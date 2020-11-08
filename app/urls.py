from django.urls import path
from . import views

app_name = 'Expense Tracker'
urlpatterns = [
    #home page
    path('', views.index, name ='index'),
    path('addExpense', views.addExpense, name ='addExpense'),
    path('saveExpense', views.saveExpense, name = 'saveExpense')

]