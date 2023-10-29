from urllib.request import urlretrieve
from pathlib import Path

def main(path :Path, args):
    URL = "https://source.unsplash.com/random/200x150.png"
    urlretrieve(URL, path)