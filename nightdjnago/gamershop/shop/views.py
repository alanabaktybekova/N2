from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'product': products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    prods = Product.objects.all()
    return render(request, 'product.html', {'products': prods})

def remot(request):
    return render(request, 'remot.html')

def video(request):
    return render(request, 'video.html')


