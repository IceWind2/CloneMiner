from distutils.core import setup
from mypyc.build import mypycify
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

setup(
    name='TextDuplicateSearch',
    version='0.1',
    description='Tool for finding duplicates in the text',
    author='Anton Glazyrin',
    ext_packages=['TextDuplicateSearch'],
    ext_modules=mypycify([
        os.path.join(dir_path, 'TextDuplicateSearch/__init__.py'),
        os.path.join(dir_path, 'TextDuplicateSearch/Tokenizer.py'),
        os.path.join(dir_path, 'TextDuplicateSearch/DuplicateData.py'),
        os.path.join(dir_path, 'TextDuplicateSearch/RepeatSearch.py'),
        os.path.join(dir_path, 'TextDuplicateSearch/SuffixArray.py')
    ]),
    install_requires=[
        'antlr4-python3-runtime',
        'nltk'
    ]
)
