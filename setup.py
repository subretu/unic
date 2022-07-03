from setuptools import setup, find_packages


setup(
    name="unitconverter",
    version="0.9.1",
    description="Python library for converting various units.",
    author="subretu",
    url="https://github.com/subretu/unit-converter",
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=False,
)
