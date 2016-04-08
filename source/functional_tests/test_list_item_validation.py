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

        # Home page refreshes, and user gets an error message saying empty lists
        # are invalid.

        # User then enters a valid item and hists enter. This works.

        # User tries again to enter empty item, error message.

        # User can correct this error by entering valid list item.
        self.fail('write me!')
