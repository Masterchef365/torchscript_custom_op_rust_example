use anyhow::Result;
use tch::{IValue, Tensor};

extern "C" {
    fn test_library();
}

fn main() -> Result<()> {
    unsafe { test_library() };
    let device = match tch::Cuda::is_available() {
        true => tch::Device::Cuda(1),
        false => {
            println!("Warning: Running on CPU");
            tch::Device::Cpu
        },
    };

    let module = tch::CModule::load_on_device("../custom_op/cell.zip", device)?;
    let kind = (tch::Kind::Float, device);
    for _ in 0..10_000 {
        let x = Tensor::rand(&[3, 4], kind);
        let h = Tensor::rand(&[3, 4], kind);
        let output = module.forward_is(&[IValue::Tensor(x), IValue::Tensor(h)])?;
        if let IValue::Tuple(mut v) = output {
            if let (Some(IValue::Tensor(a)), Some(IValue::Tensor(b))) = (v.pop(), v.pop()) {
                a.print();
                b.print();
            }
        }
    }

    Ok(())
}

