# class student
# id,fname,lname,age,dept,college_name
# 5 Objects

"""
instance variables  values are changeable
eg: self.id=id
static variable values are not changeable
eg: college_name in a college

"""
class Student:
    def setvalues(self,id,fname,lname,age,dept,college):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.dept=dept
        self.college_name=college
    def getvalues(self):
        print(self.id)
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.dept)
        print(self.college_name)

s1=Student()
s1.setvalues(1,"Anu","IG",20,"Computer","IHRD")
s1.getvalues()
print()

s2=Student()
s2.setvalues(2,"Arun","IG",27,"Electronics","ST thomas")
s2.getvalues()
print()

s3=Student()
s3.setvalues(3,"Varun","Nair",25,"Computer","IHRD")
s3.getvalues()
print()

s4=Student()
s4.setvalues(4,"Binil","D",25,"Electronics","ST thomas")
s4.getvalues()
print()

s5=Student()
s5.setvalues(5,"Anil","NP",29,"Computer","ST thomas")
s5.getvalues()
print()

