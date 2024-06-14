"""
This module contains unit tests for the main module.
"""
import unittest
from todo_app.main import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "hello")
        
if __name__ == '__main__':
    unittest.main()