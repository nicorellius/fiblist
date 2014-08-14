"""
file        :   views.py
date        :   2014-0812
module      :   lists
classes     :   
desription  :   views for lists application
"""

from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
