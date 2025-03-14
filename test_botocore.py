from importlib.metadata import version

import botocore


def test_botocore() -> None:
    assert botocore.__version__ == version("botocore")
