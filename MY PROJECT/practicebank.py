class Account:
    def __init__(self):
        self.name = input("Enter the name : ")
        self.balance = int(input("Enter the balance : "))
        self.account = int(input("Enter the accountno : "))
     
    def display(self):
        print("Name : ", self.name)
        print("Account no : ", self.account)
        print("Debit amount : ", self.amount)
        print("Credit amount : ", self.amountt)
        print("Total balance : ", self.get_balance())

    def debit(self):
        self.amount = int(input("Enter the debit amount : "))
        self.balance -=  self.amount
        print("Rs.",self.amount, "Debited successfully!")
         
        

    def credit(self):
       self.amountt = int(input("Enter the credit amount : "))
       self.balance +=  self.amountt
       print("Rs. ",self.amountt, "Credited successfully!") 
         
        

    def get_balance(self):
        return self.balance
    
    def file(self):
        return f"Name : {self.name}\nAccount No : {self.account}\nTotal balance : {self.get_balance()}\nDebit amount : {self.amount}\nCredit amount : {self.amountt}"



acc1 = Account()
acc1.debit()
acc1.credit()
acc1.display()
#with open("students.txt", "w") as f:
f = open("students.txt", "w")
f.write(acc1.file())
f.close()