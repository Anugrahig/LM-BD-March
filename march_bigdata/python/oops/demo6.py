# inheritance
# child class use properties and behaviour of parent class
# Single Inheritance

class A: # Parent Class | Super class | Base class
    def printa(self,num1):
        self.num1=num1
        print(f"Inside class A {self.num1}")
class B(A): #Child class | Derived class | subclass
    def printb(self,num2):
        self.num2=num2
        print(f"Inside Class B {self.num2}")

obj1=B()
obj1.printb(15)
obj1.printa(25)


