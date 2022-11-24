from django.contrib.auth import views as auth_views
from django.urls import path, include
from lending_site.views import IndexListView

urlpatterns = [
    path('home/', IndexListView.as_view(), name='blog-home')
]