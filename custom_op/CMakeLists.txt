cmake_minimum_required(VERSION 3.1 FATAL_ERROR)
project(test_op)

find_package(Torch REQUIRED)

# Define our library target
add_library(test_op SHARED op.cpp)
# Enable C++14
target_compile_features(test_op PRIVATE cxx_std_14)
# Link against LibTorch
target_link_libraries(test_op "${TORCH_LIBRARIES}")
