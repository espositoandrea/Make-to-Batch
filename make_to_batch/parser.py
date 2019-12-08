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
"""The command-line parser module.

This module contains the class Parser, that can be used to parse a command.
"""

class Parser:
    """A command parser.

    This class parses a command and exposes the program called, its arguments
    and its options.

    Attributes
    ----------
    program : str
        The name of the program started by the command.
    options : List[str]
        The list of options passed to the program.
    parameters : List[str]
        The list of parameters passed to the program.
    """

    def __init__(self, command: str):
        """Take a command as a string and parses it."""
        segments = command.split(' ')
        self.program = segments[0]
        segments = segments[1:]
        self.options = list()
        self.parameters = list()
        all_parameters = False
        for segment in segments:
            if segment == '--':
                all_parameters = True
            elif segment.startswith('-') and not all_parameters:
                self.options.append(segment)
            else:
                self.parameters.append(segment)
