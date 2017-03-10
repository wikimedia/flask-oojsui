import os
from distutils.core import setup

from setuptools import find_packages


def requirements(fname):
    return [line.strip()
            for line in open(os.path.join(os.path.dirname(__file__), fname))]

setup(
    name='flask-oojsui',
    version="0.0.3",
    author='Aaron Halfaker',
    author_email='aaron.halfaker@gmail.com',
    packages=find_packages(),
    scripts=[],
    url='https://pypi.python.org/pypi/flask-oojsui/',
    license=open('LICENSE').read(),
    description='This library provides python Flask utilities and static ' +
                'assets for rendering Wikimedia UI elements',
    include_package_data=True,
    long_description=open('README.md').read(),
    install_requires=requirements("requirements.txt"),
    test_suite='nose.collector',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
