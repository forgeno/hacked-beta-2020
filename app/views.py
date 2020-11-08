from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Expense

def index(request):
    return render(request, 'index.html')

def addExpense(request):
    return render(request, 'addExpense.html')

def saveExpense(request):
    if request.method == 'GET':
        try: 
            store = request.POST.get('store')
        except ValueError:
            return None
        print('1')
        try:
            date = request.POST.get('date')
        except AttributeError:
            return None
        print('2')
        try:
            amount = request.POST.get('amount')
        except Exception:
            return None
        print('3')
        try:
            name = request.POST.get('item')
        except Exception:
            return None
        print('4')
        try:
            category = request.POST.get('category')     # stored attirbutes
        except Exception:
            return None
        print('5')
        #date item cost store category
        createdObject = Expense.Create(store, amount, cost, store, category)  #created an object and store those attirbutes
        createdObject.save()    # saved the object
    return render(request, 'index.html')

