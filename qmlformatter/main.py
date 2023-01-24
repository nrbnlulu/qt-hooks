import glob
import platform
import sys
from pathlib import Path
from subprocess import Popen
import argparse
import os

def main():
    if 'Windows' in platform.platform():
        print("windows not is not supported yet.")
        return
    shared_o = Path(__file__).parent / 'lib'
    shared_o.resolve(True)
    os.chdir(shared_o)

    qmlformat = 'qmlformat'
    if platform.system() == 'Windows':
        qmlformat += '.exe'
    qml_format = Path(__file__).parent / qmlformat
    assert qml_format.exists()
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()
    files = args.filenames
    p = Popen(
        args=[str(qml_format), *files, '--inplace']
    )
    p.wait(2000)
    while p.poll() is None:
        ...
    sys.exit(p.returncode)


if __name__ == "__main__":
    main()
