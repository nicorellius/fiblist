# file: test_simple_list_creation.py
# date: 2014-0811
# description: functional tests for fiblist project


from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Testing basic app functionality.
class NewVisitorTest(FunctionalTest):

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

        self.assertEqual(input_box.get_attribute('placeholder'),
                         'Enter a To-Do item')

        # User types in "some list item" into text box.
        input_box.send_keys('some list item')

        # When user hits enter, the page updates and the
        # list item is saved.
        input_box.send_keys(Keys.ENTER)

        user_list_url = self.browser.current_url

        self.assertRegex(user_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: some list item')

        # The field is still present, so uer can add
        # another list item ("some other list item").
        # The, as before, user hits enter, page updates
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('some other list item')
        input_box.send_keys(Keys.ENTER)

        # Check fr list items in table rows
        self.check_for_row_in_list_table('2: some other list item')
        self.check_for_row_in_list_table('1: some list item')

        # New user, user2, visits site
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Leah visits home page and no sign of Nick's lists
        # First, make sure browser opened with correct page.
        self.browser.get(self.server_url)

        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertNotIn('some list item', page_text)
        self.assertNotIn('some other list item', page_text)

        # User2 starts new list by entering text ("yet another list item")
        # into the form field
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('yet another list item')
        input_box.send_keys(Keys.ENTER)

        # User2 gets her own unique URL
        user2_list_url = self.browser.current_url

        self.assertRegex(user2_list_url, '/lists/.+')
        self.assertNotEqual(user2_list_url, user_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertNotIn('some list item', page_text)
        self.assertIn('yet another list item', page_text)

        # End user story
        # self.fail('Finish the test!')
