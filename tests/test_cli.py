import pathlib
import tempfile

from make_to_batch.cli import run_with_args

_SIMPLE_MAKEFILE = """
print:
\techo 'This is a line'
"""


class TestCli:
    def test_simple_demo(self):
        with tempfile.NamedTemporaryFile('w') as srcf:
            pathlib.Path(srcf.name).write_text(_SIMPLE_MAKEFILE)

            with tempfile.NamedTemporaryFile('r') as dstf:
                run_with_args(['-i', srcf.name, '-o', dstf.name])

                dst_text = pathlib.Path(dstf.name).read_text()
                assert "IF /I \"%1\"==\"print\" GOTO print" in dst_text
                assert 'GOTO error' in dst_text
                
                assert ":print" in dst_text
                assert "echo 'This is a line'" in dst_text
