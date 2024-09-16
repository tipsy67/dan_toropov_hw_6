from django.urls import path
from catalog.views import categories, orders, ProductCreateView, ContactDetailView, ProductListView, ProductDetailView, \
    itsok, FeedbackCreateView, CategoryCreateView, ProductVersionCreateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactDetailView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('categories/', categories, name='categories'),
    path('orders/', orders, name='orders'),
    path('editor/', ProductCreateView.as_view(), name='editor'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('create_version/', ProductVersionCreateView.as_view(), name='create_version'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
    path('itsok/', itsok, name='itsok')
]
