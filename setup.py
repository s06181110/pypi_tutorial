import setuptools

__author__ = 'Enomoto Yoshiki'
__version__ = '0.0.1'
__date__ = '2019/3/1 (Created: 2019/3/1)'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='example-pkg-biva8710', \
    version=__version__, \
    author=__author__, \
    author_email='s06181110.cac@gmail.com', \
    description='A small example package', \
    long_description=long_description, \
    url='https://github.com/s06181110/pypi_tutorial', \
    packages=setuptools.find_packages(), \
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
