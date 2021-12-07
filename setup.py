from setuptools import setup

PKG="local_advent_of_code"

long_description = """A collection of reusable functions for solving advent of code"""

setup(
    name=PKG,
    python_requires = '>= 3.6',
    package_data={
        'advent_of_code': ['*.py', '__pycache__/*'],
        'advent_of_code.core': ['*.py', '__pycache__/*'],
    },
    author="Nehemiah Campbell",
    long_description=long_description,
    description='Advent of Code helpers',
    license="MIT License",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: DFSG approved",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ]
)

