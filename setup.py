import pathlib

from setuptools import setup, find_packages

setup(
    name="long_term_risk_return",
    version="0.0.1",
    python_requires=">=3.8",
    description="Study of long-term risk and returns of S&P 500 Total Returns (TR) Index",
    long_description_content_type="text/markdown",
    url="https://github.com/andersglindstrom/long_term_returns",
    author="Anders Lindstrom",
    author_email="anders@anderslindstrom.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "click>=7.0",
        "numpy>=1.19.1",
        "matplotlib>=3.3.1",
        "pandas>=1.1.1",
    ],
    entry_points={
        "console_scripts": [
            "ltr = ltr.cli:main",
        ]
    },
)
