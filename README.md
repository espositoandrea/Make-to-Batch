# Makefile to Batch

[![License](https://img.shields.io/github/license/espositoandrea/Make-to-Batch)](https://github.com/espositoandrea/Make-to-Batch/blob/master/LICENSE)
[![GitHub release (latest by
date)](https://img.shields.io/github/v/release/espositoandrea/Make-to-Batch?include_prereleases)](https://github.com/espositoandrea/Make-to-Batch/releases/latest)
[![PyPI](https://img.shields.io/pypi/v/make-to-batch)](https://pypi.org/project/make-to-batch/)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=espositoandrea_Make-to-Batch&metric=alert_status)](https://sonarcloud.io/dashboard?id=espositoandrea_Make-to-Batch)

This is a simple tool to convert a GNU Makefile into a Windows Batch file.

## Usage

Install the tool by using [PyPI](https://pypi.org/project/make-to-batch/) using
the following command:

```bash
pip install make-to-batch
```

You can also install by downloading the source code:

```bash
cd path/to/source/
python setup.py install
```

The tool provides only a command, `make-to-batch`, that converts a Makefile in
the current directory to a batch file in the same directory. The tool behaviour
can be customized using some options: here is the help of the tool.

```text
$ make-to-batch -h
usage: make-to-batch [-h] [-v] [-i INPUT] [-o OUTPUT]

Convert a Makefile to a Batch (Windows) file.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -i INPUT, --input INPUT
                        set the makefile to be converted. Defaults is
                        './Makefile'
  -o OUTPUT, --output OUTPUT
                        set he name of the output batch file. Defaults is
                        './make.bat'
```

## Contributing

For more information on how to contribute, go to the file
[CONTRIBUTING.md](CONTRIBUTING.md)
