from pathlib import Path
from importlib import import_module

def give(path :Path, args):
    ext = path.suffix
    main = import_module(f"{ext}", "givemeone.ext").main
    main(path, args)