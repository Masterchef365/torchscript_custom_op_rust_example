cmake_minimum_required(VERSION 3.19 FATAL_ERROR)
project(test_op LANGUAGES CXX CUDA)

find_package(Torch REQUIRED)

# Define our library target
add_library(test_op SHARED 
    op.cpp 
    op.cu
)
set_target_properties(test_op PROPERTIES CUDA_SEPARABLE_COMPILATION ON)

# Enable C++14
target_compile_features(test_op PRIVATE cxx_std_14)

# Link against LibTorch
target_link_libraries(test_op "${TORCH_LIBRARIES}")
