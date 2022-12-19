"""cattery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from frontsite.views import index,about,contact_func,cats_blog,cat_info
from core.views import error_404_view
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact_us/',contact_func,name='contact_us'),
    path('valerian_admin/',include('backsite.urls',namespace='panel')),
    path('blog/',include('frontsite.urls',namespace='front')),
    path('our_cats/',cats_blog,name='cats_blog'),
    path('our_cats/<int:id>',cat_info,name='cat_info'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.error_404_view'
handler500 = 'core.views.error_500_view'
