from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("tech with time!")

def v1(response):
    return HttpResponse("<h1>View1</h1>")