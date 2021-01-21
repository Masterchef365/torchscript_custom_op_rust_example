# Linux & Windows
1. Install PyTorch through Anaconda https://pytorch.org/get-started/locally/
2. Install Rust through Rustup https://rustup.rs/
3. Install CMake https://cmake.org/
4. Compile the custom operator
    1. Create a new build directory called `build`.
    2. Descend into said directory; run the script `../cmake_path.sh` which will run CMake with the correct arguments
    3. Run `make`
5. Run the script to build and serialize the model in the directory above (`./script.py`)
6. Change directories into `executor`
    1. Source `set_env.sh`, which contains environment variables needed by the build system and also for execution
    2. Run `cargo run` to build and run the executor

# Windows
Pip seems to work okay on Windows. Make sure to have the latest CMake installed. Open Developer PowerShell for VS 2019. Pass `-G "Visual Studio 16 2019"` to cmake, and open the solution. Make sure to build for release. When building the executor, do not do so from Developer PowerShell, rather from regular PowerShell