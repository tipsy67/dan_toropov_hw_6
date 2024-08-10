from django.urls import path
from catalog.views import index, contacts, product, categories, orders
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk_product>', product, name='product'),
    path('categories/', categories, name='categories'),
    path('orders/', orders, name='orders'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)