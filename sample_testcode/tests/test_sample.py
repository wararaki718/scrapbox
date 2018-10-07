'''
sample unit test
'''

import unittest
from app import sample


class TestSample(unittest.TestCase):
    def test_message_1(self):
        self.assertEqual(sample.Sample().message(), 'hello')
    
    def test_message_2(self):
        self.assertEqual(sample.Sample().message(), 'world')

if __name__ == "__main__":
    unittest.main()
