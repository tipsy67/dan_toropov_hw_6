from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogCreateView

appname = BlogConfig.name

urlpatterns = [
   path ('blog/', BlogListView.as_view(),name='blog_list'),
   path('new_blog/', BlogCreateView.as_view(), name='blog_create')
]