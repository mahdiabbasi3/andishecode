from django.shortcuts import render
from . import models

def show_plane(request):
    return render(request,'product_module/plane.html')

def show_example(request):
    product=models.Product.objects.filter(is_active=True)
    return render(request,'product_module/example.html',{'product':product})
