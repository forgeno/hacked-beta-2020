from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, world. You're in the expense tracker app.")

def index(request):
    return HttpResponse("Hello, world. You're in the expense tracker app.")

# Create your views here.
