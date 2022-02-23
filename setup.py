from setuptools import setup
from mypyc.build import mypycify
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

setup(
    name='TextDuplicateSearch',
    version='0.0.1',
    description='Tool for finding duplicates in the text',
    author='Anton Glazyrin',
    py_modules=['TextDuplicateSearch.__init__'],
    ext_modules=mypycify([
        '--disallow-untyped-defs',
        os.path.join(dir_path, 'TextDuplicateSearch/Interface.py'),
        os.path.join(dir_path, 'TextDuplicateSearch/Tokenizer.py'),
        os.path.join(dir_path, 'TextDuplicateSearch/DuplicateData.py'),
        os.path.join(dir_path, 'TextDuplicateSearch/RepeatSearch.py'),
        os.path.join(dir_path, 'TextDuplicateSearch/SuffixArray.py')
    ]),
    install_requires=[
        'nltk'
    ]
)
