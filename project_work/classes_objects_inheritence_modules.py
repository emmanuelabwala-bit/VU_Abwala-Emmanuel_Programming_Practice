# Topic 5: Classes, Objects, Inheritance, Encapsulation, Polymorphism, Modules and Packages

# 1. Creating a class
class Student:
    pass

student1 = Student()

# 2. Class attributes
class StudentInfo:
    name = "Emmanuel"
    age = 20

student2 = StudentInfo()

print(student2.name)
print(student2.age)

# 3. The __init__ method
class StudentProfile:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student3 = StudentProfile("John", 20)
student4 = StudentProfile("Mary", 22)

print(student3.name)
print(student4.name)

# 4. Methods
class StudentIntroduction:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

student5 = StudentIntroduction("John")
student5.introduce()

# 5. Inheritance
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()

# 6. Polymorphism
class DogAnimal:
    def sound(self):
        print("Woof")

class CatAnimal:
    def sound(self):
        print("Meow")

dog_animal = DogAnimal()
cat_animal = CatAnimal()

dog_animal.sound()
cat_animal.sound()

# 7. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)

account = BankAccount(500000)
account.show_balance()

# 8. Modules
# Create a file named math_tools.py:
#
# def multiply(a, b):
#     return a * b
#
# Then create main.py:
#
# import math_tools
#
# print(math_tools.multiply(5, 4))
#
# You can also import one function:
#
# from math_tools import multiply
#
# print(multiply(5, 4))
