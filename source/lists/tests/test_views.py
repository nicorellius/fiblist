"""
file        :   test_views.py
date        :   2014-0811
module      :   lists/tests
classes     :   
description :   view tests for the lists application
"""

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item, List


class SmokeTest(TestCase):
    
    def test_bad_math(self):
        
        self.assertEqual(1 + 1, 2)
        
        
class NewListTest(TestCase):
    
    def test_saves_post_request(self):
    
        self.client.post(
            '/lists/new',
            data={
                'item_text': 'A new list item'
            }
        )
        
        self.assertEqual(Item.objects.count(), 1)
        
        new_item = Item.objects.first()
        
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_post(self):
        
        response = self.client.post(
            '/lists/new',
            data={
                'item_text': 'A new list item'
            }
        )

        new_list = List.objects.first()
        
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/lists/{0}/'.format(new_list.id))
        
        
class ListViewTest(TestCase):
    
    def test_displays_only_items_for_that_list(self):

        correct_list = List.objects.create()
        Item.objects.create(text='item 1', list=correct_list)
        Item.objects.create(text='item 2', list=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='other item 1', list=other_list)
        Item.objects.create(text='other item 2', list=other_list)
        
        response = self.client.get('/lists/{0}/'.format(correct_list.id))
        
        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')

    def test_uses_list_template(self):

        list_ = List.objects.create()
        response = self.client.get('/lists/{0}/'.format(list_.id,))

        self.assertTemplateUsed(response, 'list.html')

    def test_list_passes_correct_list_to_template(self):

        # other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.get('/lists/{0}/'.format(correct_list.id))

        self.assertEqual(response.context['list'], correct_list)


class NewItemList(TestCase):

    def test_can_save_post_request_to_existing_list(self):

        # other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/{0}/add_item'.format(correct_list.id),
            data={
                'item_text': 'New item for existing list'
            }
        )

        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()

        self.assertEqual(new_item.text, 'New item for existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):

        # other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/{0}/add_item'.format(correct_list.id),
            data={
                'item_text': 'New item for existing list'
            }
        )

        self.assertRedirects(response, '/lists/{0}/'.format(correct_list.id))


class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        
        self.assertEqual(response.content.decode(), expected_html)
