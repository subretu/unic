from setuptools import setup, find_packages


setup(
    name="unit_converter",
    version="1.0.0",
    description="Python library for converting various units.",
    author="subretu",
    url="https://github.com/subretu/unit-converter",
    packages=find_packages("unit_converter"),
    package_dir={"": "unit_converter"},
    zip_safe=False,
)
