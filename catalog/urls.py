from django.urls import path
from catalog.views import home, contacts, product, categories, orders, editor

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk_product>', product, name='product'),
    path('categories/', categories, name='categories'),
    path('orders/', orders, name='orders'),
    path('editor/', editor, name='editor'),

]
