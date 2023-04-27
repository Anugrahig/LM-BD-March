# class student
# id,fname,lname,age,dept,college_name
# 5 Objects

"""
instance variables  values are changeable and we can reuse
eg: self.id=id
static variable values are not changeable
eg: college_name in a college

"""
class Student:
    college_name="IHRD"
    # instance are defined in methods are not defined outside class
    # static variable are defined outside methods
    # static variables are constants
    def setvalues(self,id,fname,lname,age,dept):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.dept=dept

    def getvalues(self):
        print(self.id)
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.dept)
        print(Student.college_name)

s1=Student()
s1.setvalues(1,"Anu","IG",20,"Computer")
s1.getvalues()
print()

s2=Student()
s2.setvalues(2,"Arun","IG",27,"Electronics",)
s2.getvalues()
print()

s3=Student()
s3.setvalues(3,"Varun","Nair",25,"Computer")
s3.getvalues()
print()

s4=Student()
s4.setvalues(4,"Binil","D",25,"Electronics")
s4.getvalues()
print()

s5=Student()
s5.setvalues(5,"Anil","NP",29,"Computer")
s5.getvalues()
print()

