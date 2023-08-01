#MUMBERE ASINGYA JOSHUA
# 2100713667
# 21/U/13667/EVE



#Floats, strings, int, lists, dictionaries, char, booleans
#variables store data that is of different type

#LISTS, TOOPLES, DICTIONARIES, SETS

# w = 'sorry'
# z = 77
# y = 1j
# print(type(w))
# print(type(z))
# print(type(y))

# #1. LISTS
# """
# lists are used to store in a single variable
# inbuilt datatype
# use square brackets
# they are ordered and can be changed
# allows duplicated values
# """
# students = ["Martha","Rogers","Trisha"]
# Students = ["Martha","Rogers","Trisha", "Martha", "Rogers"] #duplicate
# print(students)
# print(Students)

# #operations on lists
# print(len(Students))
# print(Students[0])
# print(Students[-3])
# Students[1]= "Birimumaaso"
# print(Students)
# Students.append("Tenyigwa") #adding items at the end
# print(Students)
# Students.insert(1,"luyombo") #adding items at a specified position
# print(Students)
# Students.remove("Trisha")
# print(Students)
# Students.pop(0)
# print(Students)
# print(type(Students))
# # print(Students[1:3]) #This line retrieves elements from index 1 to index 2 (exclusive)
# # print(Students[:3]) #Here, the slice starts from the beginning of the list and goes up to index 2
# # print(Students[3:]) #starts from index 3 and goes until the end of the list
# # print(Students[:]) #[:] retrieves all elements in the list, effectively creating a copy of the original list.
# # print(Students[::2]) #The step value 2 skips every second element. It starts from the beginning 
# # print(Students[::-1]) #The negative step value -1 reverses the list, so all elements are returned in reverse order.
# # print(Students[::-2]) #negative step value -2 selects every second element in reverse order. It starts from the end of the list




# #2. TUPLES
# """
# Store items in a single variable
# yuples are ordered and unchangable
# uses ()
# """
# phones = ("samsung", "iPhone", "Techno", "samsung", "iPhone")
# print(phones)

# #using for loops
# for x in phones:
#     print(x)

# #operations in a tuple
# Tuple1 =("rice", "meat")
# Tuple2= (100, 400, 600)
# print(Tuple1)
# # print(type(Tuple1))

# #exercise how to access turples and indexing and length
# print(Tuple1[0])
# print(len(Tuple1))

# #adding the items in a tuple(change it to a list 1st)
# z = list(phones)
# z.append("Nokia")
# phones = tuple(z)
# print(phones)

# # adding two tuples 
# laptops = ("Dell","HP","Acer")
# laptop = ("samsung",)
# laptops += laptop
# Newstock = laptops + laptop
# print(Newstock)
# print(laptops)



# #3. SETS
"""
store multiple items in a single variable
unchangeable but can remove and add some variables
unordered and dont allow duplicates
{}
"""
""" 
set1 = {"rice", "meat","beans","peas"}
print(set1)

#exercise find length, data type, accessing items, add items, add two sets
print(len(set1))
print(type(set1))
set1.add("yams")
print(set1)

set2 = "eggplant"
print(set1.union(set2))

for i in set1:
    print(i)
"""

#----------------------------------------------------------------



#####DAY 2
""" 
#DICTIONARIES
Used to store values in key:value pairs
they are ordered and changeable but dont allow duplicate
can have data of different types
"""
#Examples
"""
myDict = {
    "name": "Rogers",
    "age": 99,
    "gender": "male"
}

print(myDict)
#length of dictionary
print(len(myDict))
print(type(myDict))

#Access to dictionary
print(myDict["name"])
print(myDict.get("gender"))
print(myDict.values())
print(myDict.keys())
"""
"""EXERCISES ON DICTIONARY
return all the values
check if a key exits in the dictionary
changing dictionary items
updating dictionary items
how to add dictionary items
how to remove dictionary items
loop through a dictionary 


<<<<< see below>>>>>
"""
"""
#updating an item in the dictionary
myDict["gender"] = "male"
print(myDict)

#Adding an item in the dictionary
myDict["height"] = 180
print(myDict)

#Deleting an item in the dictionary
del myDict["name"]
print(myDict)

#checking if key is in the dictionary
if "name" in myDict:
    print("name is in the dictionary")
else:
    print("name is not in the dictionary")

# Looping through the dictionary
for key, value in myDict.items():
    print(key, ":", value)
"""


################################################################

#NUMBERS
#integers, floats, complex numbers
# w = 10 #int
# r = 10.5 #float
# s = 44j #complex number
""" 
print(type(w))
print(type(r))
print(type(s))

#integers
a = 2
b = 27794766737
c = -54674894038
print(type(a))
print(type(b)))
print(type(c))

#floats
h = 2.9
g = 27.794766737
f = -54.674894038
print(type(h))
print(type(g))
print(type(f))

#complex numbers
a = 10 + 2j
b = 27794766737j
c = -5j
print(type(a))
print(type(b))
print(type(c))


#type conversions
w = 10 #int
r = 10.5 #float
s = 5 + 3j #complex number

#Exercises on conversions

print(int(r)) #change float  to int
print(complex(r)) #change float to complex number
print(complex(w)) #change int to complex number
# print(int(s))
# print(float(s))
"""

################################

#CASTING
"""
works mostly when we want to specify cariable type
"""

# x= int(20)
# y = int(300000) 
# z = int("8") # a is 8

# print(x)
# print(y)
# print(z)

################################################################


# #STRINGS
# print ("Afternoon")
# print ('Evening')

# #Assign string to variable
# w = "Afternoon"
# print(w)

# #Multiline string
# q="""
# I am offering BSSE
# year three 
# Currently doing recess in python, data science and Django
# """
# print(q)

# #Strings as arrays
# a = "Afternoon"
# print(a[1])

"""
Exercises on Strings
1.use len() to determine the length of string
2.loop through strings
3. slicing the string
4. concatenating
5.

<<<see below>>>
"""
# greet = " Hello, Welcome "
# print(len(greet))

# for x in range(len(greet)) :
#     print(greet[x])


# #How to modify strings
# print(greet.lower())
# print(greet.upper())

# #Remove whitespace
# print(greet.strip())
# print(greet.lstrip())
# print(greet.rstrip())

# #String concatenation
# a = "good "
# b = "morning"
# print(a+b)

# Format string
# age = 23
# name = "My name is martha and i am " + str(age) 

""" 
#using the format method
the formart() function takes the passed parameters, formarts them
and places them into where the place holders are
"""
# name = "My name is martha and i am {} "
# print(name.format(age))

################################################################

#BOOLEAN
#These evaluate to true or false
# print(20<50)
# print(20>50)
# print(20==20)

# print(bool(15))
# r = "Martha"
# print(bool(r))

# #Exercises
# #use a condition to show the use of boolean values
# if (20>50):
#     print("True")
# else:
#     print("False")

########### DAY 3 ############
# Assignment
# LISTS
# # 1
# people = ["caicedo", "fati", "john", "silva"]
# # 2
# people[0]= "acan"
# print (people[0])
# # 3
# people.append("ozan")
# print(people)

# # 4
# print(people[-1])

# # 5
# people.pop(3)
# print(people)

# # 6
# print(people[-1])

# # 7
# people= ["trish", "conrad", "rogers", "owen","ben"]
# print(people[2:4])

# # 8 write list of countries and make a copy of it
# country = ["USA", "Russia","Mexico", "Egypt"]
# countrycopy = country.copy()
# print(countrycopy)

# # 9 write python program to loop through
# for countries in country:
#     print("countries")

# # 10 write list of animals names and sort thrm in both ascending and descending order
# animals = ["dog", "cat", "cow", "goat"]
# # ascending
# animals.sort()
# print(animals)
# # descending
# animals.sort(reverse=True)
# print(animals)

# # 11 using the list write python program to output only animal names with the letter 'a in them
# for animal in animals:
#     if "a" in animal:
#         print(animal)

# # 12 write two lists, one containg yo first' names and other second, join the two lists
# first_names = ["mark", "codi", "trisha","rogers" ]
# second_names = ["kijjo.", "moses", "smith", "agaba"]
# print(first_names + second_names)

# # TUPLES
# # 1
# phones = ("samsung", "iphone", "techno", "redmi")
# print("My fav brand is" ,phones[1])

# # 2
# print(phones[-3])

# # 3
# phoneslist = list(phones)

# phoneslist[1] = "itel"
# phonestuple = tuple(phoneslist)
# print(phonestuple)

# # 4
# phonelist = list(phones)
# phonelist.append("Huawei")
# phone2= tuple(phonelist)
# print(phone2)

# # 5
# for phone in phones:
#     print(phone)

# # 6
# deletinglist = list(phones)
# deletinglist.pop(0)
# newphones = tuple(deletinglist)
# print(phone)

# # 7
# tuple3 = tuple(["Kampala", "Gulu", "Kasese", "Jinja"])
# print(tuple3)

# # 8
# names = ("Trisha", "Martha")
# first_name, last_name = names
# print(first_name)
# print(last_name)

# # 9
# tuple3 = tuple(["Kampala", "Tororo", "Kabale", "Gulu"])
# print(tuple3[1:])

# # 10
# first_name = "Rogers"
# sec_name = "Tenyigwa"
# full_name = first_name + sec_name
# print(full_name)

# # 11
# colors = ("red", "pink","blue")
# multiplied = colors*3
# print(multiplied)

# # 12
# thistuple = (1,3,7,8,7,5,4,6,8,5)
# numberoftimes = thistuple.count(8)
# print(numberoftimes)


# # SETS

# # 1
# beverages = set(("juice", "water", "smirnoff"))
# print(beverages)

# # 2
# beverages.add("porridge")
# beverages.add("tea")
# print(beverages)

# # 3
# mySet = {"oven","kettle","microwave","refrigerator"}
# print("microwave" in mySet)

# # 4
# mySet.remove("kettle")
# print(mySet)

# # 5
# for item in mySet:
#     print(item)

# # 6
# mySet = {"oven","kettle","microwave","refrigerator"}
# mySecondSet = {"cup","glass"}
# x= set(mySecondSet)
# print(mySet.union(x))

# # 7
# ages= {4,6,3}
# first_name= {"Trisha", "Esther", "Michaela"}
# joint_set = ages.union(first_name)
# print(joint_set)

# # STRINGS
# # 1
# x = 6
# y= "Rogers"

# print(str(x) +y)

# # 2
# txt=" Hello, Uganda!"
# print(txt.strip())

# # 3
# print(txt.upper())

# # 4
# replaced = txt.replace('U', 'V')
# print(replaced)

# # 5
# y= "I am proudly Ugandan"
# print(y[1:4])

# # 6
# x = ''


           

# # 6
# p= "All data scientists are cool"
# print(p)



# # DICTIONARIES
# # 1
# shoes = {
#     "brand" : "Nick",
#     "color" : "black",
#     "size" : 40
# }
# print(shoes["size"])

# # 2
# shoes["brand"] = "Adidas"

# shoes["type"] = "sneakers"

# # 4
# keys = shoes.keys()
# print(keys)

# # 5
# values = shoes.values()
# print(values)

# # 6
# if "size" in keys:
#         print("Exists in keys")

# # 7
# for j in shoes:
#      print(shoes[j])
# # for key,value in shoes.items():
# #         print(f"{key} : {value}")

# # 8
# shoes.pop("color")
# print(shoes)
# # shoes.__delitem__("color")

# # 9
# shoes.clear()
# print(shoes)

# # 10
# person = {
#      "name" :"Birimuaaso Rogers",
#      "age" :22,
#      "hobby" : "Basketbasll"
# }
# person_copy = person.copy()

# # 11
# family = {
#                 # "child1" : { "name" : "Lisa", "year"= 12},
#                 # "child2" : { "name" : "Hannah", "year"= 8},
#                 # "child3" : { "name" : "Montana", "year"= 2}}
#      "first" : person_copy, "second": person_copy, "hobby" : person_copy}
# print(family["first"]["hobby"])


########### DAY 5 ############
import os 
#Exception Handling
#Exception handling helps to prevent your program from abruptly terminating whenerrors occu
"""
In Python, there are several built-in exceptions that can be raised when an error occurs during the execution of a program. Here are some of the most common types of exceptions in Python:

SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.

NameError: This exception is raised when a variable or function name is not found in the current scope.

IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.

KeyError: This exception is raised when a key is not found in a dictionary.

ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.

AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.

IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.

ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.

ImportError: This exception is raised when an import statement fails to find or load a module.
"""

#Below are some examples of exceptions
#ZeroDivisionError
try:
    num = 10
    dem = 0

    result = num/dem

    print(result)
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0. 

# Type error
x = 5
y = "hello"
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")

# Output: Error: cannot add an int and a str

#Example with the finally block
#The finally block runs whether there is an exception or not and it can be optional 
try:
    num = 10
    dem = 0

    result = num/dem

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is the finally block.") #This block of code always executes 

#Index Error
try:
    list_1 = [1, 2, 3]
    print(list_1[4])
except IndexError:
    print("Error: Index out of range.")

# Output: Error: Index out of range.


#Examples of Value Error,Zero Divion Error,and Exception class that catches other errorrs
def division():
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))

        result = dividend / divisor
        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter integers only.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        print("An error occurred:", e)

division()


#Attribute Error

# Python program to demonstrate
# AttributeError


class Geeks():
	
	def __init__(self):
		self.a = 'GeeksforGeeks'

# Driver's code
obj = Geeks()

# Try and except statement for
# Exception handling
try:
	print(obj.a)
	
	# Raises an AttributeError
	print(obj.b)
	
# Prints the below statement
# whenever an AttributeError is
# raised
except AttributeError:
	print("There is no such attribute")



#File Handling
"""
File handling in Python takes place in the following order:
1. Open a file
2. Read or write(perform operation)
3.Close the file

Advantages of file handling
1.Versatility
2. Flexibility
3. User friendly
4. Cross-platform support

Disadvantages of file handling
1. Erro prone
2. Security risks
3. Complexity
4. Performance 

Where the following mode is supported:

r: open an existing file for a read operation.

w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.

a:  open an existing file for append operation. It won’t override existing data.

 r+:  To read and write data into the file. The previous data in the file will be overridden.

w+: To write and read data. It will override existing data.

a+: To append and read data from the file. It won’t override existing data.


"""
# #Example that includes reading and writing data from a file
# # a file named "geeks", will be opened with the reading mode.
# file = open('geeks.txt', 'w')
# file.write('My name is Ariho Conrad\n' )
# file.write('I am 21 years old\n' )
# file.write("i love python programming\n")

# file = open('geeks.txt', 'r')


# # This will print every line one by one in the file
# for each in file:
# 	print (each)
        

# file.close()

# #To append a file
# file = open('geeks.txt', 'a')
# file.write('I am a geek')
# file.close()

# # #To delete a file
# # os.remove('geeks.txt')

# Writing to a file
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print("Input written to the file successfully.")
    except IOError:
        print("An error occurred while writing to the file.")

# Reading from a file
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except IOError:
        print("An error occurred while reading the file.")

# Test the functions
file_name = "temp.txt"
content = "Hello there, I am a dev"

write_to_file(file_name, content)
read_from_file(file_name)



#A simple python program to demostrate file operations
#Creating the file
def create_file(filename):
    try:
        with open(filename, 'w') as file:
            print("File created:", filename)
    except IOError:
        print("Error: Unable to create the file.")
#Writing to the file
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("Input written to the file successfully.")
    except IOError:
        print("Error: Unable to write to the file.")
#Appending to the file
def append_to_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
        print("Input appended to the file successfully.")
    except IOError:
        print("Error: Unable to append to the file.")
#Reading from the file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print("Data read from the file:\n", data)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: Unable to read from the file.")
#Deleting the file
def delete_file(filename):
    import os
    try:
        os.remove(filename)
        print("File deleted successfully:", filename)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")

if __name__ == "__main__":
    filename = "temp.txt"
    create_file(filename)

    content = "Hello, this is a sample content.\n"
    write_to_file(filename, content)

    append_content = "This content is appended.\n"
    append_to_file(filename, append_content)

    read_file(filename)

    delete_file(filename)
