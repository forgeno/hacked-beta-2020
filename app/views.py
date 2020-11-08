from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect


from .models import Expense

def home(request):
    table = Expense.objects.all()
    table_dict = {'transactions': table}
    return render(request, 'homepage.html',table_dict)

def addExpense(request):
    return render(request, 'addExpense.html')

def page2(request):
    return render(request, 'page2.html')

def returnHome(request):
    return render(request, 'homepage.html')

def saveExpense(request):
    if request.method == 'POST':
        try: 
            store = request.POST.get('store')
        except ValueError:
            return None
        print(1)
        try:
            date = request.POST.get('date')
        except AttributeError:
            return None
        print(2)
        try:
            amount = int(request.POST.get('amount'))
        except Exception:
            return None
        print(3)
        try:
            name = request.POST.get('item')
        except Exception:
            return None
        print(4)
        try:
            category = request.POST.get('category')     # stored attirbutes
        except Exception:
            return None
        print(5)
        #date item cost store category
        print("{},{},{},{},{}".format(date, name, amount, store, category))
        createdObject = Expense.Create(date, name, amount, store, category)  #created an object and store those attirbutes
        createdObject.save()    # saved the object
        print("okay it reached here")
    return render(request, 'homepage.html')

