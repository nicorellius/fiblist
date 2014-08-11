"""
file        :   functional_tests.py
date        :   2014-0811
module      :   ft
classes     :   
desription  :   functional tests for aersol project
"""

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

#for stock Django installation. this will probably change once app is built out
assert 'Django' in browser.title