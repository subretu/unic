from setuptools import setup, find_packages
import unit_converter

VERSION = unit_converter.__version__

setup(
    name="unit-converter",
    version=VERSION,
    description="Python library for converting various units.",
    author="subretu",
    url="https://github.com/subretu/unit-converter",
    packages=find_packages(),
    zip_safe=False,
)
