export TORCH_CUDA_VERSION=10.2
export LIBTORCH_CXX11_ABI=0
export LIBTORCH="$(python -c 'import torch.utils; from pathlib import Path; print(Path(torch.utils.cmake_prefix_path).parents[1])')"
LIBTORCH_DLLS=$(python -c "from torch.utils.cpp_extension import library_paths; [print(x, end=':') for x in library_paths(cuda=True)]")
CUSTOM_OP_PATH=$(realpath $PWD/../custom_op)
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$LIBTORCH_DLLS:$CUSTOM_OP_PATH"
