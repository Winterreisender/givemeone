from givemeone.libgivemeone import give
from argparse import ArgumentParser
import re
from pathlib import Path
from uuid import uuid4

def get_args() -> ArgumentParser:
    p = ArgumentParser()
    p.add_argument('path_or_ext', type=str)
    return p.parse_args()

def get_path(args):
    path_or_ext = args.path_or_ext

    path = None
    if re.match(r"\.[\w.]+", path_or_ext):
        ext = path_or_ext
        name = str(uuid4())
        path = Path(name + ext)
    else:
        path = Path(path_or_ext)
        
    assert not path.exists(), '文件已存在'
    return path


if __name__=='__main__':
    try:
        args = get_args()
        path = get_path(args)
        give(path, args)
        print(path)
    except Exception as err:
        print(err)