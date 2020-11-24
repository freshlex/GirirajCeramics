from django.shortcuts import render
from shop.models import Product
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
