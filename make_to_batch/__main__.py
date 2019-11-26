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
import os

import colorama

from make_to_batch.makefile import Makefile


def setup_args():
    parser = argparse.ArgumentParser(
        description='Convert a Makefile to a Batch (Windows) file.'
    )
    parser.add_argument(
        '-i', '--input',
        help="The makefile to be converted. Defaults to './Makefile'",
        default='./Makefile'
    )
    parser.add_argument(
        '-o', '--output',
        help="The name of the output batch file. Defaults to './make.bat'",
        default='./make.bat'
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"The Makefile '{args.input}' does not exists.")

    return args


def run():
    colorama.init()

    try:
        args = setup_args()
    except FileNotFoundError as e:
        print(f"{colorama.Fore.RED}ERROR: {e}{colorama.Style.RESET_ALL}")
        return

    makefile = Makefile()

    # Read the content of the Makefile
    with open(args.input, "r") as f:
        makefile.parse_file(f.read())

    # Create the output directories
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Create and write the output file
    with open(args.output, "w") as f:
        f.write(makefile.to_batch())


if __name__ == "__main__":
    run()
