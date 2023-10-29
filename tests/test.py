import unittest
import os
from pathlib import Path
from givemeone.libgivemeone import give

class MainTestCase(unittest.TestCase):
    def test_jpg(self):
        path = Path("a.jpg")
        give(path)
        self.assertTrue(os.path.exists(path))

    def test_txt(self):
        path = Path("a.txt")
        give(path)
        self.assertTrue(os.path.exists(path))

    def test_c(self):
        path = Path("a.c")
        give(path)
        self.assertTrue(os.path.exists(path))