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

from setuptools import setup

from make_to_batch import __version__ as version

with open("README.md", "r") as f:
    long_description = f.read()
    f.close()

setup(
    name="make-to-batch",
    version=version,
    description="A Makefile to Batch converter.",
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Andrea Esposito',
    author_email='esposito_andrea99@hotmail.com',
    url="https://github.com/espositoandrea/Make-to-Batch",
    packages=['make_to_batch'],
    download_url='https://github.com/espositoandrea/Make-to-Batch/archive/v{ver}.tar.gz'.format(ver=version),
    keywords=['Makefile', 'Batch', 'Shell', 'Windows', 'Linux', 'Converter'],
    install_requires=[
        "colorama",
    ],
    entry_points={
        'console_scripts': [
            'make-to-batch = make_to_batch.cli:run',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
