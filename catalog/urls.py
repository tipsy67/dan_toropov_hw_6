from django.urls import path
from catalog.views import ProductCreateView, ContactDetailView, ProductListView, ProductDetailView, \
    itsok, FeedbackCreateView, CategoryCreateView, ProductVersionCreateView, CategoryUpdateView, VersionUpdateView, \
    VersionDeleteView, CategoryDeleteView, ProductUpdateView, ProductDeleteView
from catalog.views import VersionListView, CategoryListView

app_name = 'catalog'

urlpatterns = [
    path('product/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactDetailView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category_create/', CategoryCreateView.as_view(), name='create_category'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('versions/', VersionListView.as_view(), name='versions'),
    path('version_update/<int:pk>', VersionUpdateView.as_view(), name='version_update'),
    path('version_delete/<int:pk>', VersionDeleteView.as_view(), name='version_delete'),
    path('version_create/', ProductVersionCreateView.as_view(), name='create_version'),
    path('editor/', ProductCreateView.as_view(), name='editor'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    path('itsok/', itsok, name='itsok')
]
