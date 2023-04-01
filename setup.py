from setuptools import setup, find_packages

setup(
    name='TextDuplicateSearch',
    version='1.0.0',
    description='Tool for finding duplicates in the text',
    author='Anton Glazyrin',
    packages=['TextDuplicateSearch'],
    include_package_data=True,
    install_requires=[
        'click',
        'nltk',
        'mypy'
    ]
)
