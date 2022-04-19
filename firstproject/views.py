from django.shortcuts import render
from django.http import HttpResponse

def hi(request):
    return HttpResponse("Hi bro's How are you?")
def bye(request):
    return HttpResponse('We are good..What about you??')