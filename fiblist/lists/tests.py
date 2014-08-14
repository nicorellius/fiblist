"""
file        :   tests.py
date        :   2014-0811
module      :   lists
classes     :   
desription  :   tests for the lists application
"""

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import home_page
#from .models import Item


class SmokeTest(TestCase):
    
    def test_bad_math(self):
        
        self.assertEqual(1 + 1, 2)


class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_post_request(self):
    
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        response = home_page(request)
        
        self.assertIn('A new list item', response.content.decode())
        
        expected_html = render_to_string(
            'home.html',
            {'new_item_text': 'A new list item'}
        )
        
        self.assertEqual(response.content.decode(), expected_html)
    
        #self.assertEqual(Item.objects.count(), 1)
        
        #new_item = Item.objects.first()
        
        #self.assertEqual(new_item.text, 'A new list item')