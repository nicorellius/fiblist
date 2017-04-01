"""
file: test_layout_styling.py
date: 2014-0811
description: functional tests for fiblist project
"""

from .base import FunctionalTest


class LayoutStylingTest(FunctionalTest):

    def test_layout_and_styling(self):

        # User2 goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(500, 400)

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
