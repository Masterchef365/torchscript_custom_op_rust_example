import os
_src_path = os.path.dirname(os.path.abspath(__file__))
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension
setup(
        name='cuda_extension',
        ext_modules=[
            CUDAExtension(name='_pvcnn_backend',
                extra_cflags=['-O3', '-std=c++17'],
                sources=[os.path.join(_src_path,'src', f) for f in [
                    'ball_query/ball_query.cpp',
                    'ball_query/ball_query_kern.cu',
                    #'grouping/grouping.cpp',
                    #'grouping/grouping_kern.cu',
                    #'interpolate/neighbor_interpolate.cpp',
                    #'interpolate/neighbor_interpolate_kern.cu',
                    #'interpolate/trilinear_devox.cpp',
                    #'interpolate/trilinear_devox_kern.cu',
                    #'sampling/sampling.cpp',
                    #'sampling/sampling_kern.cu',
                    #'voxelization/vox.cpp',
                    #'voxelization/vox_kern.cu',
                    'bindings.cpp',
                ]]
                )
        ],
        cmdclass={"build_ext": BuildExtension.with_options(no_python_abi_suffix=True)},
        )