from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UserConfig
from users.views import LoginView, ProfileUpdateView

appname = UserConfig.name

urlpatterns = [
   path ('login/', LoginView.as_view(), name='login'),
   path ('logour/', LogoutView.as_view(), name='logout'),
   path('profile/', ProfileUpdateView.as_view(), name='profile'),
   # path('edit_blog/<slug:slug>', BlogUpdateView.as_view(), name='blog_update'),
   # path('view_blog/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
]