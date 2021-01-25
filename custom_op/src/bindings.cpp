#include <torch/script.h>
#include <iostream>
#include "ball_query/ball_query.hpp"

#ifdef _WIN32 
extern "C" void __declspec( dllexport ) test_library() { std::cout << "Custom op loaded on Windows" << std::endl; }
#else
extern "C" void test_library() { std::cout << "Custom op loaded on Linux" << std::endl; }
#endif

TORCH_LIBRARY(_pvcnn_backend, m) {
    m.def("ball_query", &ball_query_forward);
}
