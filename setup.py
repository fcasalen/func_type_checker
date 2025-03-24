from setuptools import setup, find_packages

setup(
    name='func_type_checker',
    version='0.1.0',
    license="GNU GENERAL PUBLIC LICENSE",
    author="fcasalen",
    author_email="fcasalen@gmail.com",
    description="package to project ensure that the function is called with the correct type of arguments",
    packages=find_packages(),
    include_package_data=True,
    install_requires=open('requirements.txt').readlines(),
    long_description=open("README.md").read(),
    classifiers=[
        "Development Status :: 5 - Prodution/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12"
    ]
)
