[![build\test](https://github.com/IceWind2/TextDuplicateSearch/actions/workflows/python-app.yml/badge.svg)](https://github.com/IceWind2/TextDuplicateSearch/actions/workflows/python-app.yml)
# TextDuplicateSearch

A universal tool for finding strict and near duplicates in text documents.

## Getting Started

### Prerequisites

* python 3.8+
* pip

### Installation

1. Clone the repo
   ```commandline
   git clone https://github.com/IceWind2/TextDuplicateSearch.git 
   ```
2. Install requirements
   ```commandline
   pip install -r requirements.txt
   ```
3. Install necessary NLTK data
   ```commandline
   python -m nltk.downloader stopwords wordnet punkt
   ```
4. (optional) Install package
   ```commandline
   pip install .
   ```

## Usage

### CLI

**Important:** always use `-m` when executing commands

Use `--help` to see available options

```commandline
python -m TextDuplicateSearch --help
```

### Package

```python
import TextDuplicateSearch as tds

cfg = tds.create_config()
cfg.input_file = "text.txt"
cfg.output_file = "output.txt"
   
tds.strict_search(cfg)
```