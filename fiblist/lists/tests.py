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
from .models import Item


class SmokeTest(TestCase):
    
    def test_bad_math(self):
        
        self.assertEqual(1 + 1, 2)
        
        
class NewListTest(TestCase):
    
    def test_saves_post_request(self):
    
        self.client.post(
            '/lists/new',
            data = {'item_text': 'A new list item'}
        )
        
        self.assertEqual(Item.objects.count(), 1)
        
        new_item = Item.objects.first()
        
        self.assertEqual(new_item.text, 'A new list item')
        
        
    def test_redirects_after_post(self):
        
        response = self.client.post(
            '/lists/new',
            data = {'item_text': 'A new list item'}
        )
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/lists/some-list/')
        
        
class ListViewTest(TestCase):
    
    def test_displays_all_items(self):
        
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')
        
        response = self.client.get('/lists/some-list/')
        
        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
        
        
    def test_uses_list_template(self):
        
        response = self.client.get('/lists/some-list/')
        
        self.assertTemplateUsed(response, 'list.html')

class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
        
    def test_home_page_returns_correct_html(self):
        
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        
        self.assertEqual(response.content.decode(), expected_html)