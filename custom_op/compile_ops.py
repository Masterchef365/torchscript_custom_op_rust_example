import os
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
setup(
        name='cuda_extension',
        ext_modules=[
            CUDAExtension(name='_pvcnn_backend',
                extra_cflags=['-O3', '-std=c++17'],
                sources=[os.path.join('src', f) for f in [
                    'ball_query/ball_query.cpp',
                    'ball_query/ball_query_kern.cu',
                    'bindings.cpp',
                ]]
                )
        ],
        cmdclass={"build_ext": BuildExtension.with_options(no_python_abi_suffix=True)},
        )