from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'Expense Tracker'
urlpatterns = [
    path('', views.home, name ='home'),
    path('addExpense', views.addExpense, name ='addExpense'),
    path('saveExpense', csrf_exempt(views.saveExpense), name = 'saveExpense')

]