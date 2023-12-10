from setuptools import setup
from Cython.Build import cythonize

setup(
    name="Cythonised backtracking with MRV which takes c arrays",
    ext_modules=cythonize("bt_mrv.pyx"),
)

# run python setup.py build_ext --inplace
