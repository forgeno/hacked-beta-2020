from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    # return HttpResponse("Hello, world. You're in the expense tracker app.")
    return render(request, 'homepage.html')

# Create your views here.
