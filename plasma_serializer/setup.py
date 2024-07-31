from setuptools import setup, find_packages

setup(
    name="plasma_serializer",
    version="0.1",
    packages=find_packages(),
    install_requires=["pyarrow==9.0.0", "numpy"],
)
