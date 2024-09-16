
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, Contact, Feedback, Category, ProductVersion
from catalog.forms import ProductForm, CategoryForm, ProductVersionForm

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

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class ContactDetailView(DetailView):
    template_name = 'catalog/contacts.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:contacts',
    }
    context_object_name = 'data'

    def get_object(self, **kwargs):
        queryset = Contact.objects.order_by('-updated_at')
        obj = queryset.first()
        return obj


class ProductDetailView(DetailView):
    model=Product
    template_name = 'catalog/product.html'
    extra_context = {
        'menu': menu,
        'item_selected': '',
        }

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
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
    return redirect('catalog:home')


def categories(request):
    return redirect('catalog:home')

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'title_form': 'Добавить категорию'
    }
    success_url =  reverse_lazy('catalog:home')

class ProductVersionCreateView(CreateView):
    model = ProductVersion
    form_class = ProductVersionForm
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'title_form': 'Добавить версию'
    }
    success_url =  reverse_lazy('catalog:home')