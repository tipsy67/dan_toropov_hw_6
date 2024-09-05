from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from blog.models import Blog
from catalog.views import menu


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'menu': menu,
        'item_selected': 'blog:blog_list',
    }


    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blog/editor.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'blog:blog_list',
        'title_form': 'Добавить статью'
    }
    success_url =  reverse_lazy('blog:blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published']
    template_name = 'blog/editor.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'blog:blog_list',
        'title_form': 'Изменить статью'
    }
    success_url = reverse_lazy('blog:blog_list')

class BlogDetailView(DetailView):
    model = Blog
    extra_context = {
        'menu': menu,
        'item_selected': 'blog:blog_list',
    }
