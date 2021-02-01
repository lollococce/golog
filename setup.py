# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="golog",
    version="0.4.9",
    author="Lorenzo Coacci",
    author_email="lorenzo@coacci.it",
    description="The package contains some useful general functions for logging, monitoring and more.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/lollococce/golog",
    keywords=['logging', 'monitoring', 'alerts'],
    license=license,
    include_package_data=True,
    install_requires=[
        'sphinx',
        'pytest',
        'twine',
        'sphinx_rtd_theme',
        'sphinx',
        'termcolor',
        'alive_progress',
        'twilio',
        'slackclient',
        'validators'
    ],
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ]
)
