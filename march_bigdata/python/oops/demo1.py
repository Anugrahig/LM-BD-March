# Class,object and reference creation

"""
Class => function => Methods
self => instance keyword => for creating instance variables
 instance : we can use same variable in another function


"""


class Person:
    def reading(self):
        print("Reading a book")

    def writing(self):
        print("Writing a book")


obj1 = Person()
obj1.reading()
obj1.writing()

per2 = Person()
per2.writing()
