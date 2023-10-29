from pathlib import Path

def main(path :Path):
    with open(path,'w') as f:
        f.write('Hello')
    