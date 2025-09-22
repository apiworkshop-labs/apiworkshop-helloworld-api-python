import unittest
from src.app import build_message

class TestHelloWorld(unittest.TestCase):
    def test_without_name(self):
        result = build_message({})
        self.assertEqual(result, "Hello, World!")

    def test_with_name(self):
        result = build_message({"name": ["Alice"]})
        self.assertEqual(result, "Hi Alice,\nHow are you?")

if __name__ == "__main__":
    unittest.main()
