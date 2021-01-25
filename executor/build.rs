fn main() {
    let mut current_dir = std::env::current_dir().unwrap();
    current_dir.pop();
    current_dir.push("custom_op");
    println!("cargo:rustc-link-search={}", current_dir.into_os_string().into_string().unwrap());
    println!("cargo:rustc-link-search={}", r"C:\Users\dunca\Documents\torchscript_custom_op_rust_example\custom_op\build\temp.win-amd64-3.8\Release\Users\dunca\Documents\torchscript_custom_op_rust_example\custom_op\src\ball_query\");// what the fuck
    println!("cargo:rustc-link-lib={}", "_pvcnn_backend");
}