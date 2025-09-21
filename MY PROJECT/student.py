class student:
   
    def __init__(self):
      self.name = input("Enter the name : ")
      self.rollno = int(input("Enter the rollno :"))
      self.subject = input("Enter the subject : ")
      self.marks = float(input("Enter the marks : "))


    def display(self):
        print("name : ", self.name)
        print("Rollno : ", self.rollno)
        print("Subject : ", self.subject)
        print("Marks : ", self.marks)

    def file(self):
        f = open("students.txt", "w")
        f.write(f"{"name : ",self.name},\n{self.rollno},\n{self.subject},\n{self.marks}\n")
        f.close()


s1 = student()
s1.display()
s1.file()