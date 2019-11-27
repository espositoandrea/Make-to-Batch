# Makefile to Batch

[![License](https://img.shields.io/github/license/espositoandrea/Make-to-Batch?style=for-the-badge)](https://github.com/espositoandrea/Make-to-Batch/blob/master/LICENSE)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/espositoandrea/Make-to-Batch?style=for-the-badge)](https://github.com/espositoandrea/Make-to-Batch/releases/latest)

This is a simple tool to convert a GNU Makefile into a Windows Batch file.

## Usage

Install the tool by using [PyPI](https://pypi.org/project/make-to-batch/) using the following command:

```bash
pip install make-to-batch
```

You can also install by downloading the source code:

```bash
cd path/to/source/
python setup.py install
```

The tool provides only a command, `make-to-batch`, that converts a Makefile in the current directory to a batch file in the same directory. The tool behaviour can be customized using some options: here is the help of the tool.

```fundamental
$ make-to-batch -h
usage: make-to-batch [-h] [-i INPUT] [-o OUTPUT]

Convert a Makefile to a Batch (Windows) file.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The makefile to be converted. Defaults to './Makefile'
  -o OUTPUT, --output OUTPUT
                        The name of the output batch file. Defaults to
                        './make.bat'

```
