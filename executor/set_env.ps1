#!/usr/bin/env bash
#$DLL_PATH=$(Resolve-Path "$PWD\..\custom_op\build\Release")
#$Env:TORCH_CUDA_VERSION=10.1
#$Env:LIBTORCH_CXX11_ABI=0
#$Env:LIBTORCH="$(python -c 'import torch.utils; from pathlib import Path; print(Path(torch.utils.cmake_prefix_path).parents[1])')"
#$Env:PATH="$Env:LIBTORCH\lib;$DLL_PATH;$Env:PATH"

$Env:TORCH_CUDA_VERSION=10.1
$Env:LIBTORCH_CXX11_ABI=0
$Env:LIBTORCH="$(python -c 'import torch.utils; from pathlib import Path; print(Path(torch.utils.cmake_prefix_path).parents[1])')"
$LIBTORCH_DLLS=$(python -c "from torch.utils.cpp_extension import library_paths; [print(x, end=';') for x in library_paths(cuda=True)]")
$CUSTOM_OP_PATH=$(Resolve-Path $PWD\..\custom_op)
$Env:PATH="$Env:PATH;$LIBTORCH_DLLS;$CUSTOM_OP_PATH"