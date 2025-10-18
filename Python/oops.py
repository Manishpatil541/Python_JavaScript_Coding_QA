# Object Oriented Programmming in Python
# The main concept of OOPs is to bind the data and the functions that work on that together as a single unit
#  so that no other part of the code can access this data.


# Polymorphism
# The word polymorphism means having many forms. 
# In programming, polymorphism means the same function name is used for different types.


# class Gas:
#     def __init__(self, price, unit):
#         self.price = price
#         self.unit = unit
#     def info(self):
#         print(f"I am gas. My price is {self.price}, measured in {self.unit}.")
#     def make_sound(self):
#         print("psssssssssssssss")
# class Water:
#     def __init__(self, price, unit):
#         self.price = price
#         self.unit = unit
#     def info(self):
#         print(f"I am water. My price is {self.price}, measured in {self.unit}.")
#     def make_sound(self):
#         print("whooooooosh")
# # Driver Code
# g = Gas(0.43, 'cu/ft')
# w = Water(0.075, 'gallons')
# for amenity in (g, w):
#     amenity.make_sound()
#     amenity.info()


# Abstraction
# Abstraction in Python is the process of hiding the real implementation of an 
# application from the user and emphasizing only how to use the application.

from abc import ABC, abstractmethod
# Amenity becomes our abstract base class (ABC)
class Amenity(ABC):
    def turn_on(self):
        pass
# We extend our ABC to three new child classes
class Electricity(Amenity):
    def turn_on(self):
        print("You flipped the light switch!")
class Water(Amenity):
    def turn_on(self):
        print("You pressed the faucet up!")
class Gas(Amenity):
    def turn_on(self):
        print("You turned the knob on the stovefront!")
# Driver code
# W = Electricity()
# W.turn_on()
# E = Water()
# E.turn_on()
# G = Gas()
# G.turn_on()


# Inheritance
# Inheritance is the capability of one class to derive or inherit the properties from another class. 
# The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class. The benefits of inheritance are:

# It represents real-world relationships well.
# It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
# It is transitive in nature

# Types of Inheritance – 
# Single Inheritance:
# Single-level inheritance enables a derived class to inherit characteristics from a single-parent class.

# Multilevel Inheritance:
# Multi-level inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.

# Hierarchical Inheritance:
# Hierarchical level inheritance enables more than one derived class to inherit properties from a parent class.

# Multiple Inheritance:
# Multiple level inheritance enables one derived class to inherit properties from more than one base class.

# Example
# Python code to demonstrate how parent constructors
# are called.

# parent class
# class Person():
# 	def __init__(self, name, idnumber):
# 		self.name = name
# 		self.idnumber = idnumber

# 	def display(self):
# 		print(self.name)
# 		print(self.idnumber)
		
# 	# def details(self):
# 	# 	print("My name is {}".format(self.name))
# 	# 	print("IdNumber: {}".format(self.idnumber))
	
# # child class
# class Employee(Person):
# 	def __init__(self, name, idnumber, salary, post):
# 		self.salary = salary
# 		self.post = post

# 		# invoking the __init__ of the parent class
# 		Person.__init__(self, name, idnumber)
		
# 	def details(self):
# 		print("My name is {}".format(self.name))
# 		print("IdNumber: {}".format(self.idnumber))
# 		print("Post: {}".format(self.post))


# # creation of an object variable or an instance
# a = Employee('Rahul', 886012, 200000, "Intern")

# # calling a function of the class Person using
# # its instance
# a.display()
# a.details()


# Polymorphism
# Polymorphism simply means having many forms. 
# For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.

# class Bird():
#     def intro(self):
#         print("Thera are many types of birds")

#     def fly(self):
#         print("most of birds will fly but some cannot")

# class Sparrow(Bird):
#     def fly(self):
#         print("sparrow will fly")

# class Ostrich(Bird):
#     def fly(self):
#         print("ostrich cannot fly becaues of its too height")

# obj_1 = Bird()
# obj_2 = Sparrow()
# obj_3 = Ostrich()

# obj_1.intro()
# obj_1.fly()

# obj_2.intro()
# obj_2.fly()

# obj_3.intro()
# obj_3.fly()


# Encapsulation

# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). 
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent the accidental 
# modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s 
# method. Those types of variables are known as private variables.


class Base:
    def __init__(self):
        self.a = "VaibhavBorgave"
        self.__c = "VaibhavBorgave"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
# Driver code
obj1 = Base()
print(obj1.a)