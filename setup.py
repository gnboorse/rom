import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rom",  # Replace with your own username
    version="0.0.1",
    author="Gabriel Boorse",
    author_email="gnboorse@gmail.com",
    description="Python Roman Numeral Parsing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gnboorse/rom",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 2 - Pre-Alpha",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    python_requires='>=3.6',
)
