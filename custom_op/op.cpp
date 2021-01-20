#include <torch/script.h>
#include <cstdio>

torch::Tensor test_op(torch::Tensor blarg, torch::Tensor warg) {
    return blarg + warg + warg;
}

TORCH_LIBRARY(my_ops, m) {
    m.def("test_op", test_op);
}

extern "C" void test_library() { std::cout << "Custom op loaded" << std::endl; }
