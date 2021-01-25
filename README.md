# Prerequisites
* PyTorch through Anaconda https://pytorch.org/get-started/locally/ (pip seems to work on Windows)
* Rust through Rustup https://rustup.rs/
* Nvidia CUDA Toolkit 10.1
* C++ Compiler and build system (Visual Studio 2019 on Windows)

# Instructions
1. Compile the custom op in `custom_ops`
    * Linux: Run `sh compile_ops.sh`
    * Windows: Open the directory in `x64 Native Tools Command Prompt for VS 2019`. Run `compile_ops.bat`
2. Serialize the model by running (`script.py`)
3. Change directories into `executor`
    1. Set environment variables; `source set_env.sh` on Linux or `set_env.ps1` on Windows
    2. Run `cargo run` to build and run the executor
        * On Windows, make sure to run this in regular PowerShell or Command Prompt; build tools interfere
        * Note that this may not work in release mode at the moment; see [this issue](https://github.com/LaurentMazare/tch-rs/issues/291)