from pathlib import Path

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.template.defaultfilters import first
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Contact, Feedback
from .forms import AddProduct

menu = [{'title': "Главная", 'url_name': 'catalog:home', 'svg_name': 'home', 'visibility': True},
        {'title': "Категории", 'url_name': 'catalog:categories', 'svg_name': 'speedometer2', 'visibility': True},
        {'title': "Заказы", 'url_name': 'catalog:orders', 'svg_name': 'table', 'visibility': True},
        {'title': "Контакты", 'url_name': 'catalog:contacts', 'svg_name': 'people-circle', 'visibility': True},
        # {'title': "Редактор", 'url_name': 'catalog:editor', 'svg_name': 'grid', 'visibility': True},
        {'title': "Статьи", 'url_name': 'blog:blog_list', 'svg_name': 'collection', 'visibility': True},
        ]


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

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:editor',
        'title_form': 'Добавить товар'
    }
    success_url =  reverse_lazy('catalog:home')

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        # 'item_selected': 'catalog:editor',
        'title_form': 'Обратная связь'
    }
    success_url =  reverse_lazy('catalog:itsok')

def itsok(request):
    context = {
        'menu': menu,
    }
    return render(request, 'catalog/itsok.html', context=context)


def orders(request):
    pass


def categories(request):
    pass

