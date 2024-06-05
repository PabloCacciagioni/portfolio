"""
This module contains unit tests for the main module.
"""
import unittest
from todo_app.main import hello

class TastHello(unittest.TestCase):
    def test_hello(self):
        """
        Test the hello function.
        """
        self.assertEqual(hello(), "hello")
        
if __name__ == '__main__':
    unittest.main()