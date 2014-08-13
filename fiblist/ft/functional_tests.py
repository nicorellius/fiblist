"""
file        :   functional_tests.py
date        :   2014-0811
module      :   ft
classes     :   
desription  :   functional tests for aersol project
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        
        # Check the title and be sure it's what we expect
        self.assertIn('To-Do', self.browser.title)
        
        # Confirm header mentions the title of page
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # User is invited to enter a to-do item in application.
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a To-Do item'
        )
    
        # User types in "some list item" into text box.
        input_box.send_keys('some list item')
        
        # When user hits enter, the page updates and the list item is saved.
        input_box.send_keys(Keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        
        self.assertTrue(
            any(row.text == '1: some list item' for row in rows),
            "New To-Do item not found in table."
        )
        
        # The field is still present, so uer can add another list item, if desired.
        
        # User is concerned whether this site will actually remember the items entered.
        # The site generates a URL for each list item, so this is good.
        
        # User clicks the URL and notices the list item is there.
        
        # End user story
        self.fail('Finish the test!')
        
        
if __name__ == '__main__':
    
    unittest.main(warnings='ignore')