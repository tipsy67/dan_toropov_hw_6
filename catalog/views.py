import csv
import os.path
from pathlib import Path

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib import messages

from catalog.models import Product, Contact, Feedback

PATH_TO_CSV = Path(__file__).parent.joinpath('data', 'feedback.csv')

menu = [{'title': "Главная", 'url_name': 'home', 'svg_name': 'home', 'visibility': True},
        {'title': "Категории", 'url_name': 'categories', 'svg_name': 'speedometer', 'visibility': True},
        {'title': "Заказы", 'url_name': 'orders', 'svg_name': 'table', 'visibility': True},
        {'title': "Контакты", 'url_name': 'contacts', 'svg_name': 'home', 'visibility': True}
        ]


# Create your views here.
def index(request):
    context = {
        'objects_list': Product.objects.all().order_by('-created_at'),
        'menu': menu,
        'item_selected': 'home',
    }
    return render(request, 'catalog/index.html', context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Feedback.objects.create(name=name, phone=phone, message=message)
        return render(request, 'catalog/itsok.html')
    data = Contact.objects.all()[:1]
    if data:
        data = data[0]
    context = {
        'objects_list': Product.objects.all().order_by('-created_at'),
        'menu': menu,
        'item_selected': 'contacts',
        'data': data,
    }
    return render(request, 'catalog/contacts.html', context=context)


def product(request, pk_product):
    try:
        context = {'object': Product.objects.get(pk=pk_product)}
        return render(request, 'catalog/product.html', context=context)
    except Product.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")


def orders(request):
    return index(request)


def categories(request):
    return index(request)
