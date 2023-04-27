# Inheritance - Eg:
# 1.Person
# fname,lname,age,loc
#
# 2.Employee
# id,prof,salary

# id,fname,lname,age,prof,loc,salary

class Person:
    def setperson(self,fname,lname,age,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc

class Employee(Person):
    def setemployee(self,id,prof,salary):
        self.id=id
        self.prof=prof
        self.salary=salary
    def getemployee(self):
        print(f"{self.id} {self.fname} {self.lname} {self.age} {self.prof} {self.loc} {self.salary}")

emp1=Employee()
emp1.setemployee(101,"Web Developer",125000)
emp1.setperson("Anu","IG",20,"TCR")
emp1.getemployee()
emp2=Employee()
emp2.setemployee(102,"Web Designer",25000)
emp2.setperson("Manu","Kumar",25,"TVM")
emp2.getemployee()

