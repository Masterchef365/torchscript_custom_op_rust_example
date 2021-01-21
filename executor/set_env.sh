#!/usr/bin/env bash
SHARED_PATH="$PWD/../custom_op/build/"
export TORCH_CUDA_VERSION=10.2
export LIBTORCH_CXX11_ABI=0
export LIBTORCH="$(python -c 'import torch.utils; from pathlib import Path; print(Path(torch.utils.cmake_prefix_path).parents[1])')"
export LD_LIBRARY_PATH=${LIBTORCH}/lib:$SHARED_PATH:$LD_LIBRARY_PATH