'''
sample_pytest
'''

import pytest
from app import sample

class TestSample(object):
    def test_message_1(self):
        assert sample.Sample().message() == 'hello'
    
    def test_message_2(self):
        assert sample.Sample().message() == 'world'
