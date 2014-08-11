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

assert 'Django' in browser.title #for stock Django installation