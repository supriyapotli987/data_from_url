from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def data_from_url(request,Name):
    return HttpResponse(f'hii {Name} how are you')
