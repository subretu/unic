from setuptools import setup, find_packages
import unicorn

VERSION = unicorn.__version__

setup(
    name="unicornr",
    version=VERSION,
    description="Python library for converting various units.",
    author="subretu",
    url="https://github.com/subretu/unicorn",
    packages=find_packages(),
    zip_safe=False,
)
