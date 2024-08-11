from django.urls import path
from catalog.views import index, contacts, product, categories, orders, editor


urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk_product>', product, name='product'),
    path('categories/', categories, name='categories'),
    path('orders/', orders, name='orders'),
    path('editor/', editor, name='editor'),

]
