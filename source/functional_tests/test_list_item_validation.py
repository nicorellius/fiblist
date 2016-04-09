"""
file        :   test_list_item_validation.py
date        :   2014-0811
module      :   functional_tests
classes     :
description :   functional tests for fiblist project
"""

from .base import FunctionalTest

from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):

        # User goes to the home page and enters empty item. Hits enter to submit.
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # Home page refreshes, and user gets an error message saying empty lists
        # are invalid.
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't submit an empty list item.")

        # User then enters a valid item and hists enter. This works.
        self.browser.find_element_by_id('id_new_item').send_keys('Flash light')
        self.check_for_row_in_list_table('1: Flash light')

        # User tries again to enter empty item, error message.
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # User gets empty item error message again.
        self.browser.find_element_by_id('id_new_item').send_keys('Flash light')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't submit an empty list item.")

        # User can correct this error by entering valid list item.
        self.browser.find_element_by_id('id_new_item').send_keys('Batteries')
        self.check_for_row_in_list_table('1: Flash light')
        self.check_for_row_in_list_table('1: Batteries')

        self.fail('write me!')
