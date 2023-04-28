# Constructor
"""
The constructor is method that is called when an object is created
we call object with creation time
# we can pass value with object creation,
doesn't need separate method calling
"""
class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def setvalues(self):
        print(f"{self.name} {self.age} {self.address}")
per1=Person("Anu",20,"TCR")
per1.setvalues()
per1=Person("Manu",29,"TVM")
per1.setvalues()


