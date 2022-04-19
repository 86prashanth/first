from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def keka(request):
    return HttpResponse('prashanth ambala')

def thanu(request):
    return HttpResponse("lenovo ideapad slim3 ") 
def bhanu(request):
    return HttpResponse("this is prashanth <b>Nanda</b>")