#
class Person:
    def setvalues(self,fanme,lname,age,place):
        self.fname=fanme
        self.lname=lname
        self.age=age
        self.place=place
    def printvalues(self):
        print(self.lname)
        print(self.fname)
        print(self.age)
        print(self.place)

per1=Person()
per1.setvalues("Anu","ig",24,"TCR")
per1.printvalues()

per2=Person()
per2.setvalues("Nithin","P",25,"KTM")
per2.printvalues()

per3=Person()
per3.setvalues("Manu","Nair",29,"EKM")
per3.printvalues()

per4=Person()
per4.setvalues("David","P",28,"TVM")
per4.printvalues()




