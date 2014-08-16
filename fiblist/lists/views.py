"""
file        :   views.py
date        :   2014-0812
module      :   lists
classes     :   
desription  :   views for lists application
"""

from django.shortcuts import redirect, render

from .models import Item


def home_page(request):
    
    if request.method == 'POST':
        
        Item.objects.create(text=request.POST['item_text'])
        
        return redirect('/lists/some-list/')
    
    return render(request, 'home.html')


def view_list(request):
    
    items = Item.objects.all()
    
    return render(request, 'list.html', {'items': items})
