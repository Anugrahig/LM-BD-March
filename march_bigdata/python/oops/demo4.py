# Employee
# id,fname,lname,age,prof,company_name
class Employee:
    # static variable
    company_name="hargnA IT Solutions"
    def setvalues(self,id,fname,lname,prof):
        # instance variables
        self.id = id
        self.fname = fname
        self.lname = lname
        self.prof = prof
    def getvalues(self):
        print(f"{self.id}, {self.fname} {self.lname},{self.prof},{Employee.company_name}")
e1=Employee()
e1.setvalues(100,"Manu","Nair","HR")
e1.getvalues()
print()
e2=Employee()
e2.setvalues(101,"Rajeev","P","Snr Manager")
e2.getvalues()
print()
e3=Employee()
e3.setvalues(102,"Akhil","KL","UI Designer")
e3.getvalues()
print()
e4=Employee()
e4.setvalues(103,"Manoj","NM","Web Developer")
e4.getvalues()
print()
e4=Employee()
e4.setvalues(104,"Arun","IG","DevOps Developer")
e4.getvalues()
print()





