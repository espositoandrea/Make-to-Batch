# Makefile to Batch

[![License](https://img.shields.io/github/license/espositoandrea/Make-to-Batch)](https://github.com/espositoandrea/Make-to-Batch/blob/master/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/espositoandrea/Make-to-Batch/Python%20package)](https://github.com/espositoandrea/Make-to-Batch/actions)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/espositoandrea/Make-to-Batch?include_prereleases)](https://github.com/espositoandrea/Make-to-Batch/releases/latest)
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

## License

This tool/library is free software and is released under the [MIT
License](LICENSE). You're free to copy, modify, and redistribute this tool in
any way: all I ask is some credit (just a mention is enough) and I'd love the
source code with your edits back.

The choice of the license should allow you to use the tool in any context you
like (either in free, open or proprietary contexts). If you should have any
problem with it, I first apologize because I'm not a lawyer, then just contact
me and we'll try to solve it together.

## Contributing

For more information on how to contribute, read
[this comment](https://github.com/espositoandrea/Make-to-Batch/pull/2#issuecomment-703069158)
and check the rules in the file [CONTRIBUTING.md](CONTRIBUTING.md)

### In Short: What Should I Do?

The short answer is: do whatever you want. No discussion is required to expand
the number of commands available in the translation: if you want to add new
commands or options, just add them to the [look up
table](make_to_batch/look_up_table.py) and open a PR.

Any modification to the architecture or structure of the tool is also welcomed:
just open a new issue and we'll discuss about it.

### Is there a Roadmap?

There's not an actual structured roadmap for this tool: the main thing that
needs to be done is to expand the set of recognized command.

Nonetheless, there are some enhancements I'd like to bring into this tool: I'll
leave a brief list here.

- Allow the tool to read from `stdin` and write to `stdout` (in the standard
  Unix fashion)
- Enhance the [documentation](https://make-to-batch.readthedocs.io/)
