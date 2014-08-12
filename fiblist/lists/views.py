"""
file        :   views.py
date        :   2014-0812
module      :   lists
classes     :   
desription  :   views for lists application
"""

from django.shortcuts import render


def home_page(request):
    
    return render(request, 'home.html')
