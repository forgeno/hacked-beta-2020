from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


from .models import Expense

def home(request):
    return render(request, 'homepage.html')

def addExpense(request):
    return render(request, 'addExpense.html')

def saveExpense(request):
    if request.method == 'POST':
        try: 
            store = request.POST.get('store')
        except ValueError:
            return None
        try:
            date = request.POST.get('date')
        except AttributeError:
            return None
        try:
            amount = int(request.POST.get('amount'))
        except Exception:
            return None
        try:
            name = request.POST.get('item')
        except Exception:
            return None
        try:
            category = request.POST.get('category')     # stored attirbutes
        except Exception:
            return None
        #date item cost store category
        print("{},{},{},{},{}".format(date, name, amount, store, category))
        createdObject = Expense.Create(date, name, amount, store, category)  #created an object and store those attirbutes
        createdObject.save()    # saved the object
        print("okay it reached here")
    return render(request, 'homepage.html')

