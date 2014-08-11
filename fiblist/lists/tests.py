"""
file        :   tests.py
date        :   2014-0811
module      :   lists
classes     :   
desription  :   tests for the lists application
"""

from django.test import TestCase


class SmokeTest(TestCase):
    
    def test_bad_maths(self):
        
        self.assertEqual(1 + 1, 3)
    
