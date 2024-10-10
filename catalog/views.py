from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductOwnerForm, CategoryForm, ProductVersionForm, ProductAdminForm, ProductModeratorForm
from catalog.models import Product, Contact, Feedback, Category, ProductVersion
from utils import get_categories_from_cache

menu = [{'title': "Главная", 'url_name': 'catalog:home', 'svg_name': 'home', 'visibility': True},
        {'title': "Категории", 'url_name': 'catalog:categories', 'svg_name': 'speedometer2', 'visibility': True},
        {'title': "Версии", 'url_name': 'catalog:versions', 'svg_name': 'table', 'visibility': True},
        {'title': "Контакты", 'url_name': 'catalog:contacts', 'svg_name': 'people-circle', 'visibility': True},
        # {'title': "Редактор", 'url_name': 'catalog:editor', 'svg_name': 'grid', 'visibility': True},
        {'title': "Статьи", 'url_name': 'blog:blog_list', 'svg_name': 'collection', 'visibility': True},
        ]


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 3
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:home',
    }
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_moderator:
            return Product.objects.all()

        return Product.objects.filter(Q(is_published=True)|Q(owner=self.request.user))


    def get_context_data(self, **kwargs):
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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {
        'menu': menu,
        'item_selected': '',
    }



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductOwnerForm
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:editor',
        'title_form': 'Добавить товар'
    }
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        user.owner = self.request.user
        user.save()

        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'catalog/editor.html'
    form_class = ProductAdminForm
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:home',
        'title_form': 'Редактировать товар',
        'footer_url': 'catalog:product_delete'
    }
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):

        user = self.request.user
        if user.is_superuser:
            return ProductAdminForm
        elif user == self.object.owner:
            return ProductOwnerForm
        elif user.is_moderator:
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete.html'
    success_url = reverse_lazy('catalog:home')
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:home',
        'title': 'Удаление товара',
        'title_card': 'товар',
        'title_href': {'url': 'catalog:product_update'},
    }

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['name', 'phone', 'message']
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        # 'item_selected': 'catalog:editor',
        'title_form': 'Обратная связь'
    }
    success_url = reverse_lazy('catalog:itsok')


def itsok(request):
    context = {
        'menu': menu,
    }
    return render(request, 'catalog/itsok.html', context=context)


class VersionListView(LoginRequiredMixin, ListView):
    model = ProductVersion
    paginate_by = 4
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:versions',
    }

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_moderator:
            return ProductVersion.objects.all()

        return ProductVersion.objects.filter(product__owner=self.request.user)


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductVersion
    form_class = ProductVersionForm
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:versions',
        'title_form': 'Редактировать версию',
        'footer_url': 'catalog:version_delete'
    }
    success_url = reverse_lazy('catalog:versions')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         obj = form.save(commit=False)
    #         if obj.is_active:
    #             if obj.product.versions.filter(Q(is_active=True) & ~Q(pk=obj.pk) ):
    #                 raise ValidationError('Уже есть активная версия для этого продукта')
    #
    #     return super().form_valid(form)


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = ProductVersion
    form_class = ProductVersionForm
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:versions',
        'title_form': 'Добавить версию'
    }
    success_url = reverse_lazy('catalog:home')


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductVersion
    template_name = 'catalog/delete.html'
    success_url = reverse_lazy('catalog:versions')
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:versions',
        'title': 'Удаление версии',
        'title_card': 'версию',
        'title_href': {'url': 'catalog:version_update'},
    }


class ProductVersionCreateView(LoginRequiredMixin, CreateView):
    model = ProductVersion
    form_class = ProductVersionForm
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'title_form': 'Добавить версию'
    }
    success_url = reverse_lazy('catalog:home')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    paginate_by = 4
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:categories',
    }

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_moderator:
            return get_categories_from_cache()

        raise PermissionDenied

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:categories',
        'title_form': 'Редактировать категорию',
        'footer_url': 'catalog:category_delete'

    }
    success_url = reverse_lazy('catalog:categories')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'catalog/delete.html'
    success_url = reverse_lazy('catalog:versions')
    extra_context = {
        'menu': menu,
        'item_selected': 'catalog:versions',
        'title': 'Удаление категории',
        'title_card': 'категорию',
        'title_href': {'url': 'catalog:category_update'},
    }


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/editor.html'
    extra_context = {
        'menu': menu,
        'title_form': 'Добавить категорию'
    }
    success_url = reverse_lazy('catalog:home')
