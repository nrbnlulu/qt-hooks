import subprocess
import sys
import pytest
from qmlformatter import main
from pathlib import Path

from qmlformatter.main import IS_WINDOWS


@pytest.mark.skipif(IS_WINDOWS, "no dll's bundled currently")
def test_formats():
    sample_qml = Path(__file__).parent / 'sample.qml'
    assert sample_qml.exists()
    with open(sample_qml, 'r') as f:
        before = f.read()
    with open(sample_qml, 'w') as f:
        messed = before.replace('\n', '\n \n')
        f.write(messed)

    p = subprocess.Popen(
        ['qmlformatter', str(sample_qml.resolve())]
    )
    p.wait(2000)
    assert p.returncode == 0
    with open(sample_qml, 'r') as f:
        after = f.read()

    assert messed != after
