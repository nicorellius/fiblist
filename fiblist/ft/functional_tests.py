"""
file        :   functional_tests.py
date        :   2014-0811
module      :   ft
classes     :   
desription  :   functional tests for aersol project
"""

from selenium import webdriver
import unittest


# Testing basic app functionality.
class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # First, make sure browser opened with correct page.
        self.browser.get('http://localhost:8000')
        
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # User is invited to enter a to-do item in application.
    
        # User types in "some list item" into text box.
        
        # When user hits enter, the page updates and the list item is saved.
        
        # The field is still present, so uer can add another list item, if desired.
        
        # User is concerned whether this site will actually remember the items entered.
        # The site generates a URL for each list item, so this is good.
        
        # User clicks the URL and notices the list item is there.
        
        # End user story
        
        
if __name__ == '__main__':
    
    unittest.main(warnings='ignore')