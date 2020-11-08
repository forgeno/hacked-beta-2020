"""
HackED Beta 

Expense Logic
Author: Joseph Latina

"""
from app.models import Expense

#user is the dictionary data from user
Table = Expense(user[0],user[1],user[2],user[3],user[4])
Table.create()
Table.save()

def summary_category(category):
    entries = Table.objects.all(category=category)
    pass

entry = Table.objects.get(category=category)
"""
OLD LOGIC
#menu
def menu():
    #starting parameters
    select = 0
    Data_Table = Table()
    #open file first
    filename = "Expense Database.xlsx"
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active    
    #loop for the main menu
    while select == 0:
        print("\nMain Menu\n-------------------------------\n(0) Quit\n(1) Add Transaction\n(2) Modify transaction\n(3) Delete transaction\n(4) Print transactions\n(5) Save data")
        choice = input("Enter command: ")
        while choice not in ["0","1","2","3","4","5"]:
            choice = input("Enter command: ")           
        if choice == "1":
            entry = user_input()
            Data_Table.add(sheet,entry)
            print("Entry Added") 
            print(entry)            
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass 
        elif choice == "5":
            #save data
            wb.save(f"/Users/Grace/Desktop/HackED/hacked-beta-2020/{filename}")
            print("Data saved")
        elif choice == "0":
            print("Goodbye")
            break
    

#adding data
class Transaction:
    
    def __init__(self, date, item, cost, store, category):
        self.date = date
        self.item = item
        self.cost = float(cost)
        self.store = store
        self.category = category
        self.id = None
        
    def __repr__(self):
        return f"Date: {self.date} Item: {self.item} Cost: {self.cost} Store: {self.store} Category: {self.category}"
    
    def __eq__(self,other):
        if self.id == other.id:
            return True
        return False
    
    def create_id(self, unique_id):
        self.id = unique_id
        
    def get_data(self):
        return list(vars(self).values())
        
    def update(self, elem):
        pass
    
#class Table
class Table:
    def __init__(self):
        self.entries = 0
    
    def add(self, sheet, transaction):
        #create unique id
        entry_id = 1001 + self.entries
        transaction.create_id(entry_id)
        #find the number of rows already used
        num_of_rows = sheet.max_row
        #extract data from transaction object
        data_list = transaction.get_data()
        #add data to cells
        for i in range(6):
            data = sheet.cell(row=num_of_rows+1,column=(i+1))
            data.value = data_list[i]
        self.entries += 1
    
    def delete(self, transaction):
        pass
    
def create():
    
    #create worksheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    #Set up the columns
    tab_categories = ["Date","Item","Cost","Store","Category","ID"]
    for i in range(6):
        tab = sheet.cell(row=1,column=(i+1))
        tab.value = tab_categories[i]
        
    wb.save("/Users/Grace/Desktop/HackED/hacked-beta-2020/Expense Database.xlsx")

#user input
def user_input():
    date = input("Enter date (format: mm/dd/year): ")
    item = input("Enter the item bought: ")
    cost = input("Enter price of this item (format: 21.67): ")
    while cost.isdigit == False or "." not in cost or len(cost[cost.find(".")+1:]) != 2:
        cost = input("Enter price of this item (format: 21.67): ")
    store = input("Enter the store the item was bought from: ")
    category = input("What is the category of the item: ")
    entry = Transaction(date,item,cost,store,category)
    return entry

def load_file():
    pass
#modify data
#delete data
#print data
"""

