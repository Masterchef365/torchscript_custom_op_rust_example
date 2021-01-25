from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

setup(
    name="test_op",
    ext_modules=[
        CppExtension(
            "test_op",
            ["op.cpp"],
        )
    ],
    cmdclass={"build_ext": BuildExtension.with_options(no_python_abi_suffix=True)},
)