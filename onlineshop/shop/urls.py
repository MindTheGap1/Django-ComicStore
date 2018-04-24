from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.comic_list, name='comic_list'),
]