#include <torch/script.h>
#include <cstdio>

#ifdef _WIN32
#include <Python.h>
PyMODINIT_FUNC PyInit_test_op(void) { return NULL; }
#endif

torch::Tensor test_op(torch::Tensor blarg, torch::Tensor warg) {
    return blarg + warg + warg;
}

TORCH_LIBRARY(my_ops, m) {
    m.def("test_op", test_op);
}
