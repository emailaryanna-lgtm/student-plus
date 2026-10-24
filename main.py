# Write a program to create a class with the name Student and perform the following 
# tasks - 

# 1. Declare a variable grade
# 2. Print a sentence inside the class
# 3. Create an object of class student and see the output
class Student:
    def __init__ (self,name,grade):
        self.name=name
        self.grade=grade
    def display(self):
        print("My name is", self.name)
        print("My grade is", self.grade)
s=Student("Lily",80)
s.display()
