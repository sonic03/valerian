from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect


def error_404_view(request,exception):

    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')

def error_500_view(request,exception=None):

    return render(request, '500.html')

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
# Create your views here.
