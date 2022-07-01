from setuptools import setup


setup(
    name="unit-converter",
    version="1.0.0",
    description="Python library for converting various units.",
    author="subretu",
    url="https://github.com/subretu/unit-converter",
    packages=find_packages("unit-converter"),
    package_dir={"": "unit-converter"},
    zip_safe=False,
)
