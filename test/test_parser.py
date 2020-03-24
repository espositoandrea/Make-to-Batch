import pytest
from make_to_batch.parser import Parser

class TestParser:
    def test_init(self):
        parser = Parser('rm -r --verbose dir1 dir2')
        assert hasattr(parser, 'program')
        assert hasattr(parser, 'options')
        assert hasattr(parser, 'parameters')
        assert 'rm' == parser.program

        assert '-r' in parser.options
        assert '--verbose' in parser.options
        assert '-f' not in parser.options
        assert '--force' not in parser.options

        assert 'dir1' in parser.parameters
        assert 'dir2' in parser.parameters
        assert 'other_dir' not in parser.parameters
