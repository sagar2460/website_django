from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(requests):
    return HttpResponse('NAVEEN KUMAR & INDU DEVI')


def family(requests):
    return HttpResponse('THIS IS MY FAMILY')


