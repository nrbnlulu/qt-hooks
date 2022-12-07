import sys
from pathlib import Path
from subprocess import Popen

import PySide6


def main(files: list[str]):
    qml_format = Path(PySide6.__file__).parent / 'qmlformat'
    assert qml_format.exists()
    p = Popen(
        args=[str(qml_format), *files, '--inplace']
    )
    p.wait(2000)
    while p.poll() is None:
        ...
    sys.exit(p.returncode)


if __name__ == "__main__":
    main(sys.argv)
