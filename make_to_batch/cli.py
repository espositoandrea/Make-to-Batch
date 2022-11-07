#  MIT License
#
#  Copyright (c) 2019 Andrea Esposito
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import argparse
import locale
import os
import sys
from typing import Optional, List

import colorama

from make_to_batch import __version__
from make_to_batch.makefile import Makefile

_DEFAULT_ENCODING = locale.getpreferredencoding(False)


def setup_args(args: List[str]):
    """Set the tool's arguments.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing all the arguments values. The keys are the
        following:
        * 'input': The name of the Makefile to be converted.
        * 'output': The name of the output batch file.

    Raises
    ------
    FileNotFoundError
        If the Makefile provided via command line arguments does not exists.
    """
    parser = argparse.ArgumentParser(
        prog='make-to-batch',
        description='Convert a Makefile to a Batch (Windows) file.'
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s ' + str(__version__)
    )
    parser.add_argument(
        '-i', '--input',
        help="set the makefile to be converted. Defaults to './Makefile'",
        default='./Makefile'
    )
    parser.add_argument(
        '-o', '--output',
        help="set the name of the output batch file. Defaults to './make.bat'",
        default='./make.bat'
    )
    parser.add_argument(
        '-e', '--encoding',
        help="set the encoding of the input and output file. Defaults to %s" % (repr(_DEFAULT_ENCODING),),
        default=_DEFAULT_ENCODING,
    )

    args = parser.parse_args(args)

    if not os.path.exists(args.input):
        raise FileNotFoundError("The Makefile '{}' does not exists.".format(args.input))

    return args


def run_with_args(args: Optional[List[str]] = None):
    """The main function.

    Run the tool.
    """
    colorama.init()
    args = list(args or sys.argv[1:])

    try:
        args = setup_args(args)
    except FileNotFoundError as e:
        print(colorama.Fore.RED + "ERROR: " + str(e) + colorama.Style.RESET_ALL)
        return

    makefile = Makefile()
    encoding = args.encoding

    # Read the content of the Makefile
    with open(args.input, "r", encoding=encoding) as f:
        makefile.parse_file(f.read())

    # Create the output directories
    os.makedirs(os.path.dirname(args.output) or '.', exist_ok=True)

    # Create and write the output file
    with open(args.output, "w", encoding=encoding) as f:
        f.write(makefile.to_batch())


def run():
    return run_with_args(None)
