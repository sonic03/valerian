from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect,render
from core.views import error_404_view,error_500_view

def is_login(func):
    def wrapper(request,*args, **kwargs):
        if request.user.is_authenticated:
           return func(request,*args, **kwargs)
        else:
            return render(request, '500.html')

    return wrapper
#
# def not_authenticate(func):
#     def wrapper(request,*args, **kwargs):
#         if not request.user.is_authenticated:
#             return func(request,*args, **kwargs)
#     return wrapper

def is_panel(func):
    def wrapper(request,*args, **kwargs):
        host=request.get_host()
        if host.startswith('management'):
            return func(request,*args, **kwargs)
        else:
            return render(request, '404.html')
    return wrapper