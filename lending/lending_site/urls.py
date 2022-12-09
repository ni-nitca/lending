from django.urls import path
from lending_site.views import IndexListView


urlpatterns = [
    path(r'', IndexListView.as_view(), name='blog-home')
]
