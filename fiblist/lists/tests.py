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

    def test_home_page_can_save_post_request(self):
    
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        response = home_page(request)
        
        self.assertEqual(Item.objects.count(), 1)
        
        new_item = Item.objects.first()
        
        self.assertEqual(new_item.text, 'A new list item')
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/some-list/')
        
    def test_home_page_redirects_after_post(self):
    
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        
        response = home_page(request)
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/some-list/')

        
    def test_home_page_only_saves_items_when_necessary(self):
        
        request = HttpRequest()
        
        home_page(request)
        
        self.assertEqual(Item.objects.count(), 0)