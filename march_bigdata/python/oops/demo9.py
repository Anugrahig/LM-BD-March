# Multiple Inheritance eg:
# Person
# fname,lname,age,loc
# Profession
# qualification,year_of_exp,pass_out_year
# Employee
# id,year_joining,prof,salary

# print
# id,fname,lname,age,quali,passout,prof,salary

class Person:
    def setPerson(self,fname,lname,age,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc
class Profession:
    def setProfession(self,quali,y_of_exp,pass_year):
        self.quali=quali
        self.y_of_exp=y_of_exp
        self.pass_year=pass_year

class Employee(Person,Profession):
    def setEmployee(self,id,year_joining,prof,salary):
        self.id=id
        self.year_joining=year_joining
        self.prof=prof
        self.salary=salary

    def getEmployee(self):
        print(f"{self.id} {self.fname} {self.lname} {self.age} {self.quali} {self.pass_year} {self.prof} {self.salary}")



emp1=Employee()
emp1.setPerson("Anugrah","IG",20,"TCR")
emp1.setProfession("MTech",3,2021)
emp1.setEmployee(101,2025,"Snr Web Developer",25000)
emp1.getEmployee()