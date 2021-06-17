import os
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="nn_analysis",
    version="1.0.0",
    description="Analyse the tuning functions of neurons in artificial neural networks",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/JHoogendijk/indp-study",
    author="Jesca Hoogendijk",
    author_email="j.hoogendijk@uu.nl",
    license="GNU LGPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU LGPLv3 License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("tests", "prednet_fitting_example")),
    include_package_data=False,
    install_requires=[
        "numpy", "tqdm"
    ],
    python_requires=">=3.6",
)
