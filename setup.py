from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="requestsdantic",
    version="0.0.1",
    author="Alejo Prieto Dávalos",
    author_email="alejoprietodavalos@gmail.com",
    packages=find_packages(),
    description="requests+pydantic",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/requestsdantic/",
    project_urls={
        "Source": "https://github.com/AlejoPrietoDavalos/requestsdantic/"
    },
    python_requires=">=3.11",
    install_requires=[
        "requests>=2.32",
        "pydantic>=2.8.2"
    ],
    include_package_data=True
)
