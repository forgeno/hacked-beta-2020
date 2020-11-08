from django.db import models

# Create your models here.
class Expense(models.Model):
    date = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    store = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    
    def __repr__(self):
        return f"Date: {self.date} Item: {self.item} Cost: {self.cost} Store: {self.store} Category: {self.category}"
    
    @classmethod
    def Create(cls, date, item, cost, store, category):
        expense = cls(date = date, item = item, cost = cost, store = store, category = category)
        return expense

            
# class BudgetInfo(models.Model):

#     userBudget = models.IntegerField()

#     expenses = models.IntegerField()

#     category = models.CharField(max_length= 30)

######### READ BELOW #######
# skipped this .py file because this file is for database



