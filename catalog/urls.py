from django.urls import path
from catalog.views import categories, orders, editor, ContactDetailView
from catalog.views import ProductListView
from catalog.views import ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactDetailView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('categories/', categories, name='categories'),
    path('orders/', orders, name='orders'),
    path('editor/', editor, name='editor'),

]
