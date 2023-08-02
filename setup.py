from setuptools import setup, find_packages
import unic

VERSION = unic.__version__

setup(
    name="unic",
    version=VERSION,
    description="Python package for converting various units.",
    author="subretu",
    url="https://github.com/subretu/unic",
    packages=find_packages(),
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)
