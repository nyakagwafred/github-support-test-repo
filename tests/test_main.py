import unittest
from src.main import hello

class TestMain(unittest.TestCase):
    def test_hello(self):
        # Just check it runs
        hello()

if __name__ == "__main__":
    unittest.main()
