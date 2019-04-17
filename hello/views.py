from django.shortcuts import render
from django.app import HttpResponse

def index(request):
    return HttpResponse("Hello Django!!")

# Create your views here.
