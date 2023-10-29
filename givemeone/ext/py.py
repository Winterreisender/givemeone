from pathlib import Path

HELLOWORLD = """
if __name__ == "__main__":
    print("Hello World")
"""

def main(path :Path, args):

    with open(path,'w') as f:
        f.write(HELLOWORLD)
