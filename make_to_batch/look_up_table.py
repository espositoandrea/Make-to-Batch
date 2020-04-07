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

"""The look-up tables.

This module contains a look-up tables that can be used to convert a command from
a Makefile (Linux) to its batch equivalent. Each look-up table is a dictionary
where the keys are the Linux command and the values are dictionaries containing
the batch command and its options. The options are then stored as another
dictionary where the key represents the Linux command option and the value
represents its batch equivalent.
"""

linux_to_dos = {
    'mkdir': {
        'command': 'MKDIR',
        'options': {
            '--help': '/?',
            '-p': ''
        },
    },
    'rm': {
        'command': 'DEL /Q',
        'options': {
            '--help': '/?',
            '-f': '/F',
        },
    },
    'ls': {
        'command': 'DIR',
        'options': {
            '--help': '/?',
            '-l': '/Q',
            '-a': '/A',
            '--all': '/A',
        },
    },
    'cp': {
        'command': 'XCOPY /Y',
        'options': {
            '--help': '/?',
        },
    },
}
