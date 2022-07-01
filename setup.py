from setuptools import setup, find_packages


setup(
    name="unitconverter",
    version="1.0.0",
    description="Python library for converting various units.",
    author="subretu",
    url="https://github.com/subretu/unit-converter",
    packages=find_packages("unitconverter"),
    package_dir={"": "unitconverter"},
    zip_safe=False,
)
