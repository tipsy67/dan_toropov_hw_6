from pathlib import Path

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.template.defaultfilters import first
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contact, Feedback
from .forms import AddProduct

menu = [{'title': "Главная", 'url_name': 'catalog:home', 'svg_name': 'home', 'visibility': True},
        {'title': "Категории", 'url_name': 'catalog:categories', 'svg_name': 'speedometer2', 'visibility': True},
        {'title': "Заказы", 'url_name': 'catalog:orders', 'svg_name': 'table', 'visibility': True},
        {'title': "Контакты", 'url_name': 'catalog:contacts', 'svg_name': 'people-circle', 'visibility': True},
        {'title': "Редактор", 'url_name': 'catalog:editor', 'svg_name': 'grid', 'visibility': True},
        ]


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:home',
    }
    ordering = ['-created_at']

class ContactDetailView(DetailView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:contacts',
    }
    context_object_name = 'data'

    def get_object(self):
        queryset = Contact.objects.order_by('-updated_at')
        obj = queryset.first()
        return obj

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Feedback.objects.create(name=name, phone=phone, message=message)
        return render(request, 'catalog/itsok.html')
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model=Product
    template_name = 'catalog/product.html'
    extra_context = {
        'menu': menu,
        'item_selected': '',
        }


def orders(request):
    pass


def categories(request):
    pass

def handle_uploaded_file(f):
    with open(f"media/products/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def editor(request):
    if request.method == 'POST':
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['image'])
            product = Product(**form.cleaned_data)
            product.save()
    else:
        form = AddProduct()

    context = {
        'form': form,
        'menu': menu,
        'item_selected': 'catalog:editor',
    }
    return render(request, 'catalog/editor.html', context=context)
