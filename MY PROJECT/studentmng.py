class student:
    def __init__(self):
        self.name  = input("Enter the Name : ")
        self.rollno = int(input("Enter the Rollno : "))
        self.subject  = [None]*5
        self.marks = [0]*5
        for i in range(5):
           self.subject[i]  = input("Enter the subject : ")
           self.marks[i] = float(input(f"Enetr " ,{self.subject[i]}, f" subject marks : "))

    def display(self):
        print("Name : ",self.name)
        print("Roll no : ",self.rollno)
        total=0
        for i in range(5):
          print("Subject : ",self.subject[i])
          print("Marks : ",self.marks[i])
          total += self.marks[i]
        percentage = total/5
        print("Total : ",total)
        print("Percentage : ",percentage,"%")



s1 = student()
s1.display()        