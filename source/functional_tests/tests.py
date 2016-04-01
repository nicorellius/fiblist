"""
file        :   tests.py
date        :   2014-0811
module      :   functional_tests
classes     :   
description :   functional tests for fiblist project
"""

import sys

from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Testing basic app functionality.
class NewVisitorTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):

        cls.server_url = ''

        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://{0}'.format(arg.split('=')[1])
                return

        super().setUpClass()

        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):

        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):

        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):

        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # First, make sure browser opened with correct page.
        self.browser.get(self.server_url)
        
        # Check the title and be sure it's what we expect
        self.assertIn('Fuck-it', self.browser.title)
        
        # Confirm header mentions the title of page
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Fuck-it', header_text)
        
        # User is invited to enter a to-do item in application.
        input_box = self.browser.find_element_by_id('id_new_item')
        
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a To-Do item')
    
        # User types in "some list item" into text box.
        input_box.send_keys('some list item')
        
        # When user hits enter, the page updates and the list item is saved.
        input_box.send_keys(Keys.ENTER)
        
        nick_list_url = self.browser.current_url
        
        self.assertRegex(nick_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: some list item')
        
        # The field is still present, so uer can add another list item ("some other list item").
        # The, as before, user hits enter, page updates
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('some other list item')
        input_box.send_keys(Keys.ENTER)
        
        # Check fr list items in table rows
        self.check_for_row_in_list_table('2: some other list item')
        self.check_for_row_in_list_table('1: some list item')
        
        # New user, leah, visits site
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Leah visits home page and no sign of Nick's lists
        # First, make sure browser opened with correct page.
        self.browser.get(self.server_url)
        
        page_text = self.browser.find_element_by_tag_name('body').text
        
        self.assertNotIn('some list item', page_text)
        self.assertNotIn('some other list item', page_text)
        
        # Leah starts new list by entering text ("yet another list item") into the form field
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('yet another list item')
        input_box.send_keys(Keys.ENTER)
        
        # Leah gets her own unique URL
        leah_list_url = self.browser.current_url
        
        self.assertRegex(leah_list_url, '/lists/.+')
        self.assertNotEqual(leah_list_url, nick_list_url)
        
        page_text = self.browser.find_element_by_tag_name('body').text
        
        self.assertNotIn('some list item', page_text)
        self.assertIn('yet another list item', page_text)
        
        # End user story
        # self.fail('Finish the test!')

    def test_layout_and_styling(self):

        # Leah goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1025, 768)

        input_box = self.browser.find_element_by_id('id_new_item')

        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=5
        )

        input_box.send_keys('testing\n')
        input_box = self.browser.find_element_by_id('id_new_item')

        self.assertAlmostEqual(
            input_box.location['x'] + input_box.size['width'] / 2,
            512,
            delta=5
        )
