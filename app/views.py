from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Expense


def index(request):
    return render(request, 'index.html')

def addExpense(request):
    return render(request, 'addExpense.html')

def saveExpense(request):
    if request.method == 'POST':
        try: 
            store = int(request.POST.get('store'))
        except ValueError:
            return None
        
        try:
            date = request.POST.get('date')
        except AttributeError:
            return None
        
        try:
            amount = request.POST.get('amount')
        except Exception:
            return None
        
        try:
            name = request.POST.get('name')
        except Exception:
            return None
        
        try:
            category = request.POST.get('category')     # stored attirbutes
        except Exception:
            return None

        createdObject = Expense.objects.create(date, name, amount, store, category)  #created an object and store those attirbutes
        createdObject.save()    # saved the object
    
