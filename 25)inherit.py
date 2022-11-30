"""
What is Inheritance?

Inheritance is the ability to ‘inherit’ features or attributes from all written classes 
into newer classes we make. These features and attributes are defined data structures and
the functions we can perform with them, a.k.a. Methods. It promotes code reusability, 
which is considered one of the best industrial coding practices as it makes the codebase
modular.

In python inheritance,
new class/es inherits from older class/es. The new class/es copies all the older
class's functions and attributes without rewriting the syntax in the new class/es. 
These new classes are called derived classes, and old ones are called base classes.

For example,
inheritance is often used in biology to symbolize the transfer of genetic traits
from parents to their children. Similarly, we have parent classes (Base classes)
and child classes (derived classes). In Inheritance, we derive classes from other
already existing classes. The existing classes are the parent/base classes from which
the attributes and methods are inherited in the child classes.

Types of Inheritance in Python
Now that we are all set with the prerequisites to understand how
inheritance in python is carried out, let’s look at various inheritance types.

Single Inheritance in Python :
    

Single Inheritance is the simplest form of inheritance where a single child class is
derived from a single parent class. Due to its candid nature, it is also known as Simple
Inheritance.
#1)sigle level inheritance:-

class A():

    def GetA(self,a):
        self.a=a

    def PutA(self):
        print("A:",self.a)


class B(A):


    def GetB(self,b):
        self.b=b

    def PutB(self):
        print("B:",self.b)


a=input("enter a:")
b=input("enter b:")

ob=B()
ob.GetA(a)
ob.PutA()
ob.GetB(b)
ob.PutB()


Multiple Inheritance in Python
 
In multiple inheritance, a single child class is inherited from two or more parent
classes. It means the child class has access to all the parent classes' methods and
attributes.

However, if two parents have the same “named” methods, the child
class performs the method of the first parent in order of reference.
To better understand which class’s methods shall be executed first,
we can use the Method Resolution Order function (mro). It tells the order
in which the child class is interpreted to visit the other classes.

Multilevel Inheritance in Python

In multilevel inheritance, we go beyond just a parent-child relation.
We introduce grandchildren, great-grandchildren, grandparents, etc.
We have seen only two levels of inheritance with a superior parent class/es
and a derived class/es, but here we can have multiple levels where the parent
class/es itself is derived from another class/es.
class A:

    def GetA(self,a):
        self.a=a

    def PutA(self):
        print("A:",self.a)


class B(A):


    def GetB(self,b):
        self.b=b

    def PutB(self):
        print("B:",self.b)

class C(B):


    def GetC(self,c):
        self.c=c

    def PutC(self):
        print("C:",self.c)


a=input("enter a:")
b=input("enter b:")
c=input("enter c:")

ob=C()
ob.GetA(a)
ob.PutA()
ob.GetB(b)
ob.PutB()
ob.GetC(c)
ob.PutC()









Hierarchical Inheritance in Python

Hierarchical Inheritance is the right opposite of multiple inheritance.
It means that, there are multiple derived child classes from a single parent class.

# 3) hierarchical Inheritance:-

class A:

    def GetA(self,a):
        self.a=a

    def PutA(self):
        print("A:",self.a)


class B(A):

    def GetB(self,b):
        self.b=b

    def PutB(self):
        print("B:",self.b)
class C(A):

    def GetC(self,c):
        self.c=c

    def PutC(self):
        print("C:",self.c)
class D(A):

    def GetD(self,d):
        self.d=d

    def PutD(self):
        print("D:",self.d)

a=input("enter A:")
b=input("enter B:")
c=input("enter C:")
d=input("enter D:")


ob=B()
ob.GetA(a)
ob.GetB(b)

obc=C()
ob.GetC(c)

obd=D()
ob.GetD(d)

ob.putA()
ob.putB()
obc.putC()
obd.putD()






Hybrid Inheritance in python:

It is combination of Hierarchical & multiple Inheitance.
"""
