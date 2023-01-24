import argparse
import os
import platform
import sys
from pathlib import Path
from subprocess import Popen

IS_WINDOWS = platform.system() == "Windows"


def main():
    if IS_WINDOWS:
        print("windows not is not supported yet.")
        return
    shared_o = Path(__file__).parent / "lib"
    shared_o.resolve(True)

    qmlformat = "qmlformat.so"
    if IS_WINDOWS:
        qmlformat += ".exe"
    qml_format = Path(__file__).parent / "lib" / qmlformat
    assert qml_format.exists()
    os.chdir(shared_o)
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()
    files = args.filenames
    p = Popen(args=[str(qml_format), *files, "--inplace"])
    p.wait(2000)
    while p.poll() is None:
        ...
    sys.exit(p.returncode)


if __name__ == "__main__":
    main()
