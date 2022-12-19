from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name='frontsite'
urlpatterns = [
    path('',blogs,name='blogs'),
    path('<str:slug>/',blog_page,name='blog_page'),


]
