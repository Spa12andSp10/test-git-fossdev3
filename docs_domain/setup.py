from setuptools import setup, find_packages

setup(
    name="sales",
    version="0.0.0",
    long_description='Memory usage traker',
    long_description_content_type='text/markdown',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)