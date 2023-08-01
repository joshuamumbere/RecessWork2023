# MUMBERE ASINGYA JOSHUA
# 2100713667
# 21/U/13667/EVE



# Day Modue 2 (21-06-2023)
"""
# Control Flow
# Conditional Statements (if-elif-else)
"""
# age = 90
# if age < 18:
#     print("You are underage")
# elif age >= 18 and age <= 65:
#     print("You are an adult")
# else:
#     print("You are a senior citizen")

# Loops 
# Loops (for, while)
"""
for i in sequence:
# code
"""
# cars = ["Toyota", "Tesla", "KIA", "Jeep", "Mercedes", "Ford", "BMW"]
# for car in cars:
#     print(car)

"""
while loop: runs block of code as long as condition provided is true
"""

# Example 1
# x = 0
# while x < 5:
#     print(x)
#     x += 1

# Example 2
# fruits = ["apple", "banana", "orange", "berry"]
# fruit_count = 0
# while fruit_count < len(fruits):
#     print(fruits[fruit_count])
#     fruit_count += 1

# # Example 3
# even_number = []
# odd_number = []

# # Break and Continue statements
# # Break statement
# for number in range(1,10):
#     if number == 5:
#         break
#     print(number)

# # Continue statement
# for number in range(1,10):
#     if number == 5:
#         continue
#     print(number)

# # Exception Handling (try, except, finally)
# """
# try block: 
# except:
# finally:
# """

# try:
#     x = 10/0
# except ZeroDivisionError:
#     print("Error: Division by Zero") #cannot divide by zero
# finally:
#     print("This code is always executed") #code that's expected to run even after the exception has been caught

# # TRAILS

# # TRAIL 1
# emotion = {
#     'happy': "I'm glad to hear you are happy",
#     'sad': "I'm sorry to hear that you're feeling sad",
#     'angry': "Just take a deep breath and try to stay calm",
#     'scared': "I understand that fear can be challenging",
#     'disgusted': "I hope your are able to solve that issue at hand"
# }
# # # Prompt user to enter their emotions
# user_emotion = input("How are you feeling today?")
# # # convert user input to lowercase
# user_emotion = user_emotion.lower()

# if user_emotion in emotion:
#     print(emotion[user_emotion])
# else:
#     print("I'm sorry I don't understand that emotion")

# # TRIAL 2 (EXERCISE 1)
# # Prompt students on a scale of 1 to 10 to rate their mental health
# emotion_scale = {
#     1 : "You're feeling very low right now. Remember that you're not alone, and things will get better.",
#     2 : "You're feeling down, but don't lose hope. Reach out to your loved ones for support.",
#     3 : "You're experiencing some sadness, but remember that brighter days are ahead.",
#     4 : "You're feeling a bit blue, but there are always reasons to smile. Focus on the positive aspects of your life",
#     5 : "You're feeling neutral today. Take some time for self-care and do things that make you happy",
#     6 : "You're feeling alright, but if you ned a boost, engage in activities that bring you joy.",
#     7 : "You're feelin good an positive. Keep up the momentum and spread your happiness to others.",
#     8 : "You're in high spirits today. Share your enthusiasm with those around you and make their day better too.",
#     9 : "You're feeling fantastic! Embrace this positve energy and continue to radiate joy",
#     10 : "You're overflowing with happiness! Enjoy this incredible feeling and let it inspire you"
# }

# try:
#     print("Hello, welcome to the MUK Mental Health Portal, please follow the prompts below:")
#     user_scale = int(input("On a scale of 1 to 10, how are you feeling? \nInput: "))
#     if user_scale in emotion_scale:
#         print(emotion_scale[user_scale])
#     else:
#         print("Please input a number from 1 to 10")
# except ValueError:
#     print("You've input a string, the input should be a number from 1 to 10")
# finally:
#     print("Thank you for sharing, have a good day")

##### Using if, elif, and else ######
# try:
#     print("Hello, welcome to the MUK Mental Health Portal, please follow the prompts below:")
#     user_scale = int(input("On a scale of 1 to 10, how are you feeling? "))
#     if user_scale >= 1 and user_scale < 5:
#         print("This is low, kindly visit the university therapist for sesssions")
#     elif user_scale == 5:
#         print("This is moderate, probably a bad day?")
#     elif user_scale > 5 and user_scale <= 10:
#         print("This is great, you seem o be enjoying your experienve at the university")
#     else:
#         if user_scale > 10:
#             print("The input should be in the range of 1 to 10")
# except ValueError:
#     print("You'e input a string, the input should be a number from 1 to 10")
# finally:
#     print("Thank you for sharing, have a good day")

##############################
# DAY 3
"""
Assignment Operators

# -Membership Operators:
In: 'in' operator: Checks if a value exists in a sequence
Not in: 'not in' operator: checks if a value does not exist in a sequence

- Identity operators:
Is: 'is' operator: checks if two values are the same
Is Not: 'is not' operator checks if tw values are not the same


"""
# Examples of arithmetic operators
# # Addition
# x = 50 + 45
# print(x)
# # Subtraction
# y = 50 - 45
# print(y)
# # Multiplication
# z = 50 * 45
# print(z)
# # Division
# a = 50 / 45
# print(a)
# # Modulus
# b = 10 % 3
# print(b)
# # Exponential
# c = 50 ** 2
# print(c)

# # Examples of comparison operators
# j = 15
# t = 9

# # Greater than 
# if j > t:
#     print('j is greater than t')
#     print(j > t)
# # Greater than or equal to
# if j >= t:
#     print('j is greater than or equal to t')
#     print(j >= t)
# # Less than 
# if j < t:
#     print('j is less than t')
#     print(j > t)
# # Less than or equal to
# if j <= t:
#     print('j is less than t')
#     print(j >= t)
# # Equal to
# if j == t:
#     print('j is equal to t')
#     print(j == t)
# # Not Equal to
# if j != t:
#     print('j is equal to t')
#     print(j != t)

# Examples of Logical Operators
# r = True
# s = False

# # Logical AND
# print(r and s)

# # Logical OR
# print(r or s)

# # Logical NOT
# print(not s)

# Examples of assignment operators
# Compound assignment operators
# a = 5
# b = 6
# c = 10
# d = 8
# e = 15
# f = 2

# # Add and assign
# a += 5
# print(a)
# # Subtract and assign
# b -= 5
# print(b)
# # Multiply and assign
# c *= 5
# print(c)
# # Divide and assign
# d /= 5
# print(d)
# # Modulus and assign
# e %= 3
# print(e)
# # Exponential and assign
# f **= 3
# print(f)

# Membership assignment operators
# cars = ['Jeep', 'Tesla', 'BMW', 'Rolls Royce', 'Subaru']

# if 'Jeep' in cars:
#     print('Jeep is in the list')

# print('Jeep' in cars)
# print('Toyota' not in cars)

# Identity operators
# x = 10
# y =  10

# is operator
# print(x is y)
# print(x is not y)

# Bitwise operators
"""
These are used to perform operations on individual bits of binary numbers
Bitwise AND ('&'): Performs a bitwise AND operation between the corresponding bits of two integers
Bitwise OR ('|'): Performs a bitwise OR operation between corresponding bits of the two integers
Bitwise XOR ('^'): Performs a bitwise XOR operation
Bitwise NOT ('-'): Perform a bitwise NOT operation
Bitwise Left Shift ('<<'): Performs a left shift operation
Bitwise Rigt Shift ('>>'): Performs a right shift operation
"""

# Examples of Bitwise Operations
# a = 10
# b = 20

# # Bitwise AND
# print(a & b)
# # Bitwise OR
# print(a | b)
# # Bitwise XOR
# print(a ^ b)
# # Bitwise NOT
# print(a - b)
# # Bitwise LS
# print(a << 2)
# # Bitwise RS
# print(a >> 2)

# EXAMPLE AND ASSIGNMENT
# Create a simple calculator with the calculate function to calculate(add, subtract, multiply, divide)

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     return a / b

# def main():
#     print("SIMPLE CALCULATOR")
#     number1 = float(input("Enter the first number: "))
#     number2 = float(input("Enter the second number: "))
#     operator = input("Enter the operator (+, -, *, /): ")

#     if operator == '+':
#         print("Result of addition is:", add(number1, number2))
#     elif operator == '-':
#         print("Result of subtraction is:", subtract(number1, number2))
#     elif operator == '*':
#         print("Result of multiplication is:", multiply(number1, number2))
#     elif operator == '/':
#         print("Result of division is:", divide(number1, number2))
#     else:
#         print("Invalid operator")

# main()

# ASSIGNMENT 
# Using tkinter build a GUI calculator doing the same above.

# import tkinter as tk
"""
Here we are going to build a simple calculator with the add, subtract, multiply and divide functions
This script uses the tkinter library to enables us create GUI windows
"""

# CLICK FUNCTION - enables us to click on the differen buttons
# def click(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + str(number))

# CLEAR FUNCTION - enables us to clear the input
# def clear():
#     entry.delete(0, tk.END)

# # EQUALS FUNCTION - enables us to get the final output
# def equals():
#     expression = entry.get()
#     try:
#         result = eval(expression)
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, result)
#     except Exception:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")

# # Create the main window
# window = tk.Tk()
# window.title("Calculator")

# # Create an entry field
# entry = tk.Entry(window, width=30)
# entry.grid(row=0, column=0, columnspan=4)

# # Create buttons for numbers and operators
# button_1 = tk.Button(window, text="1", padx=20, pady=10, command=lambda: click(1))
# button_2 = tk.Button(window, text="2", padx=20, pady=10, command=lambda: click(2))
# button_3 = tk.Button(window, text="3", padx=20, pady=10, command=lambda: click(3))
# button_4 = tk.Button(window, text="4", padx=20, pady=10, command=lambda: click(4))
# button_5 = tk.Button(window, text="5", padx=20, pady=10, command=lambda: click(5))
# button_6 = tk.Button(window, text="6", padx=20, pady=10, command=lambda: click(6))
# button_7 = tk.Button(window, text="7", padx=20, pady=10, command=lambda: click(7))
# button_8 = tk.Button(window, text="8", padx=20, pady=10, command=lambda: click(8))
# button_9 = tk.Button(window, text="9", padx=20, pady=10, command=lambda: click(9))
# button_0 = tk.Button(window, text="0", padx=20, pady=10, command=lambda: click(0))

# button_add = tk.Button(window, text="+", padx=20, pady=10, command=lambda: click("+"))
# button_subtract = tk.Button(window, text="-", padx=20, pady=10, command=lambda: click("-"))
# button_multiply = tk.Button(window, text="*", padx=20, pady=10, command=lambda: click("*"))
# button_divide = tk.Button(window, text="/", padx=20, pady=10, command=lambda: click("/"))
# clear = tk.Button(window, text="C", padx=20, pady=10, command=clear) # type: ignore
# equals = tk.Button(window, text="=", padx=20, pady=10, command=equals) # type: ignore

# # Position the number buttons on the grid
# button_1.grid(row=1, column=0)
# button_2.grid(row=1, column=1)
# button_3.grid(row=1, column=2)
# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)
# button_7.grid(row=3, column=0)
# button_8.grid(row=3, column=1)
# button_9.grid(row=3, column=2)
# button_0.grid(row=4, column=1)

# # Positons of the operator buttons
# button_add.grid(row=1, column=3)
# button_subtract.grid(row=2, column=3)
# button_multiply.grid(row=3, column=3)
# button_divide.grid(row=4, column=3)

# # Positions of the action buttons
# clear.grid(row=4, column=0)
# equals.grid(row=4, column=2)

# # Start the main event loop
# window.mainloop()


##############################
# DAY 4
#   OBJECT - ORIENTED PROGRAMMING(00P)
"""
- Class
- Object
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
"""

""" Class
What is it?
It is a blueprint for creating objects.
"""

# # Example 1: Car
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start_engine(self):
#         print("Starting the engine")

#     def stop_engine(self):
#         print("Stopping the engine")

# my_car = Car("Benz", "Volkswaggen", "2022")
# print(my_car.make)
# print(my_car.model)
# print(my_car.year)
# my_car.start_engine()
# my_car.stop_engine()

# #Example 2. Bank Account
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount :
#           self.balance -= amount
#         else :
#             print("Insufficient funds")

#     def display_balance(self):
#         print("Account no: " + str(self.account_number))
#         print("Balance: ",self.balance)

# #create bank object
# bank_1 = BankAccount(2104, 5000)

# #operations
# bank_1.display_balance()
# bank_1.deposit(5000)
# bank_1.display_balance()
# bank_1.withdraw(6000)
# bank_1.display_balance()

# #Example 3. Rectangle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# #create an object
# rect_1 = Rectangle(10, 5)

# print(rect_1.area())
# print(rect_1.perimeter())


# #Example 3. Student

# class Student:
#     def __init__(self, name, year, course):
#         self.name = name
#         self.year = year
#         self.course = course

#     def display_details(self):
#         print("Name: ", self.name)
#         print("Year: ", self.year)
#         print("Course: ", self.course)

# # creating an object
# std_1 = Student("Rogers",  3, "BSSE")
# std_1.display_details()


#2.  OBJECT
"""
An object is an instance of a class.
"""

# # Example 1: Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greeting(self):
#         print("Hello " , self.name)
#         print("I am " + str(self.age) + " years old")

# #create a person object
# person_1 = Person("Martha", 3)
# person_2 = Person("Hellen", 44)
# print(person_1.name)
# person_1.greeting()
# person_2.greeting()


# # Exercise 1: claculate the area and circumference of a circle

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
    
#     def circumference(self):
#         return 2 * 3.14 * self.radius
    
# circle_1 = Circle(radius=12)
# print(circle_1.area())
# print(circle_1.circumference())

# # EXERCISE 2: 
# # Calculate and display employees(0.5 of salary) bonuses
# # emp 1 salary = 150000
# # emp 2 salary = 230000

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.bonus = 0.5 * self.salary
    
#     def display_details(self):
#         print("Name: ", self.name)
#         print("Salary: ", self.salary)
#         print("Bonus: ", self.bonus)

# #creating objects
# employee_1 = Employee("Tenyigwa", 70000)
# employee_2 = Employee("Moses", 450000)

# employee_1.display_details()
# employee_2.display_details()


#3. ENCAPSULATION
"""
Goals;
- Data hiding
- protect objects from changes
- protect objects from external changes
- code organization and modularity
"""

# # Example: with bank accounts
# class BankAccount:
#     def __init__(self, acc_no, balance):
#         self._acc_no = acc_no # encapsulates the account number attribute
#         self._balance = balance # encupsuates the balance attribute

#     def deposit(self, amount):
#         self._balance += amount
    
#     def withdraw(self, amount):
#         if self._balance >= amount :
#             self._balance -= amount
#         else :
#             print("Insufficient funds")
    
#     def get_balance(self):
#         return self._balance
    
# #create new object
# bank_2 = BankAccount(2103, 5000)
# #access the bank object and modify its properties
# print(bank_2.get_balance())
# bank_2.deposit(5000)
# print(bank_2.get_balance())
# bank_2.withdraw(6000)
# print(bank_2.get_balance())

# #Exercise 2. Convert temperature from celsius to fahrenheit

# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius
#         self._fahrenheit = (celsius * 9 / 5) + 32

#     def get_fahrenheit(self):
#         return self._fahrenheit
    
# #creating an object
# temp_1 = Temperature(45)
# print(my_temperature.get_fahrenheit())


# ASSIGNMENT 1. Show encapsulation with employee informatiom to give a pay incrementatiom
#Salary with employee informatiom to new_salary eg from 850000 to 1000000

# class Employee:
#     def __init__(self, name, salary):
#         self._name = name
#         self._salary = salary
        
#     def new_salary(self):
#         new_salary = self._salary + (self._salary * 0.1)
#         return new_salary
    
#     def display_details(self):
#         print("Name: ", self._name)
#         print("Salary: ", self._salary)
#         print("New Salary: ", self.new_salary())

# #creating an object
# my_employee = Employee("Tenyigwa", 650000)
# my_employee.new_salary()
# my_employee.display_details()


##############################
# DAY 5
# #Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating...")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking...")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} is meowing...")

# #Create Animal objects
# animal = Animal("Generic Animal")
# dog = Dog("Rex")
# cat = Cat("Casper")

# #Invoke call eat method
# animal.eat()
# dog.eat()
# dog.bark()

# #Example2 Demostrating inheritance
# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
    
#     def display_info(self):
#         print("Brand:", self.brand)
#         print("Color:", self.color)
    
#     def move(self,)

# class Car(Vehicle):

# #Exercise 1
# #Demostrate the use of inheritance to calculate area and perimeter of a circle and a rectangle
# #respectively (Shape: circle)    
# class Shape:
#     def __init__(self, radius):
#         self.radius = radius

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__(radius)

#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# class Rectangle(Shape):
#     def __init__(self, width, length):
#         super().__init__(width)
#         self.length = length

#     def area(self):
#         return self.width * self.length
    
#     def perimeter(self):
#         return 2 * (self.width + self.length)

# #Area and perimeter of Circle 
# circle_1 = Circle(12)
# print("Area of circle: ", circle_1.area())
# print("Perimeter of circle: ", circle_1.perimeter())

# #Area and perimeter of Rectangle
# rect_1 = Rectangle(10, 20)
# print("Area of rectangle: ", rect_1.area())
# print("Perimeter of rectangle: ", rect_1.perimeter())


# #Example 3
# #Multiple Inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating...")

# class Flyable:
#     def fly(self):
#         print(f"{self.name} is flying...")

# class Bird(Animal, Flyable):
#     def __init__(self, name, species):
#         super().__init__(name)
#         self.species = species

#     def display_info(self):
#         super().display_info()
#         print("Species:", self.species)
#         print("Name: {self.name}")

# # Create a Bird object
# my_bird = Bird("Pigeon","bird")

# # Invoke the bird methods
# my_bird.eat()
# my_bird.fly()

# #Method Overriding

# class Animal:
#     def make_sound(self):
#         print("Animal is making a sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Dog is making a sound")

# class Cat(Animal):
#     def make_sound(self):
#         print("Cat is making a sound")

# def make_animal_sound(animal):
#     animal.make_sound()

# # create objects
# animal = Animal()
# dog = Dog()
# cat = Cat()

# #Calling the make_animal_sound function
# make_animal_sound(animal)
# make_animal_sound(dog)
# make_animal_sound(cat)

#Polymorphism
#Polymorphism allows you to write code that can work with different objects
#Method overriding occurs when a derived class (child class), provides its own implementation of a method that is already defined in its subclass
#Method overloading allows a class to have multiple ethods withthe same name but different parameters

# #Example 4
# class Shape:
#     def calculate_area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         return self.length * self.width
    
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius
    
# # Create shaoe objects 
# rectangle = Rectangle(10,10)
# circle = Circle(10)

# # Calculate and display the area
# print("Area of Rectangle:", rectangle.calculate_area())
# print("Area of Circle:", circle.calculate_area())

# #Abstraction 
# #Allows you to focus on essential features and hide them from unecessary details

# #Example 5: Demostration of abstraction
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     # @abstractmethod
#     def start(self):
#         pass
#     # @abstractmethod
#     def stop(self):
#         pass

# class Truck(Vehicle):
#     def start(self):
#         print("Truck is starting...")
#     def stop(self):
#         print("Truck is stopping...")
    
# #Create Vehicle objects
# truck = Truck() 

# #Start the car
# truck.start()

# #Exercise2 Demostrate abstraction using calculating area of a circle and rectangle
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self,name):
#         self.name = name
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,name,radius):
#         super().__init__(name)
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
# class Rectangle(Shape):
#     def __init__(self,name,length,width):
#         super().__init__(name)
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width

# #Create Shape objects
# circle = Circle("Circle",20)
# rectangle = Rectangle("Rectangle",14,14)

# #Calculate and display the area
# print("Area of Circle:", circle.area())
# print("Area of Rectangle:", rectangle.area())


#Assignment 1: Deadline 01 July 2023
#Create a receipt printing program with GUI interface, a mere advanced detail earns you more points
import tkinter as tk
from tkinter import messagebox

def print_receipt():
    # Get input values from the entry fields
    customer_name = customer_name_entry.get()
    item_name = item_name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()

    # Validate the input fields
    if customer_name == "":
        messagebox.showerror("Error", "Please enter the customer name.")
        return

    if item_name == "":
        messagebox.showerror("Error", "Please enter the item name.")
        return

    if quantity == "" or not quantity.isdigit():
        messagebox.showerror("Please enter a valid quantity.")
        return

    if price == "" or not price.replace(".", "").isdigit():
        messagebox.showerror("Please enter a valid price.")
        return

    # Calculate the total cost
    total_cost = float(quantity) * float(price)

    # Create the receipt message
    receipt_message = f"Customer Name: {customer_name}\n"
    receipt_message += f"Item: {item_name}\n"
    receipt_message += f"Quantity: {quantity}\n"
    receipt_message += f"Price: {price}\n"
    receipt_message += f"Total Cost: {total_cost}\n"

    # Display the receipt message in a message box
    messagebox.showinfo("Receipt", receipt_message)

# Create the main window
window = tk.Tk()
window.title("Receipt Printing Program")

# Create labels and entry fields for input
customer_name_label = tk.Label(window, text="Customer Name:")
customer_name_label.pack()
customer_name_entry = tk.Entry(window)
customer_name_entry.pack()

item_name_label = tk.Label(window, text="Item Name:")
item_name_label.pack()
item_name_entry = tk.Entry(window)
item_name_entry.pack()

quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Create the Print Receipt button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Start the Tkinter event loop
window.mainloop()

#In this program we do not at units to our quantity and cuurency to our price