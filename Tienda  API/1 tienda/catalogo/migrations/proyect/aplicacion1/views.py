from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (requests):
    return HttpResponse ("hello ")
    #return "hello world"
def home (requests):
    return HttpResponse("hello word")