"""
Setup module to compile .pyx cython file
To compile the cython file, run: python setup.py build_ext --inplace
"""

from setuptools import setup
from setuptools import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("bt_mrv", ["bt_mrv.pyx"])]

for e in ext_modules:
    e.cython_directives = {"embedsignature": True}

setup(
    name="Cythonised backtracking with MRV which takes c arrays",
    cmdclass={"build_ext": build_ext},
    ext_modules=ext_modules,
)
