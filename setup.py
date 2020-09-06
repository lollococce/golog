import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="golog",
    version="0.4.4",
    author="Lorenzo Coacci",
    author_email="lorenzo@coacci.it",
    description="The package contains some useful general functions for logging, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lollococce/golog",
    packages=setuptools.find_packages(),
    keywords='',
    license='MIT',
    include_package_data=True,
    install_requires=[
       'termcolor',
       'alive_progress',
       'twilio',
       'slackclient',
       'validators'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ]
)