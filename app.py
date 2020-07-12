# drawing a shape
print("   /|")
print("  / |")
print(" /  |")
print("/___|")


# Data Types

# variable with a string
character_name = "John"

# variable with a number as a string
character_age = "35"

# variable with a number
age = 35

# variable with number in decimals
age_in_decimal = 35.222

# variable with boolean
is_male = True

print("There once was a man named " + character_name + ", ")
print("He was " + character_age + " years old.")

character_name = "Mike"

print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

#working with Strings
# new line in a string
# \ is an escape character
print("Giraffe \nAcademy")

# string variable
phrase = "Hello World"
print(phrase)

# concatonating a string
print(phrase + " my name is Loralie")

# built in python functions
# put to upper case
print(phrase.upper())

# built in python functions
# puts to upper case then checks for upper case and returns boolean
print(phrase.upper().isupper())

# built in python functions
# checking the length of a string
print(len(phrase))

# built in python functions
# finding a character by index on a string to get the character returned
print(phrase[3])

# built in python functions
# finding the index of a character and getting the index returned
print(phrase.index("W"))

# built in python functions
# replacing a word in a string
print(phrase.replace("Hello", "Welcome"))

# working with numbers
# number
print(2)

# decimal
print(2.2)

# negative numbers
print(-2.2)

# adding
print(2+2)

# subtraction
print(2-2)

# division
print(2/2)

# multiplication
print(2*2)

# order of oporations
print(2 * 10 + 5)
# more specific
print(3 * (4 + 5))

# modulas operator
# 10 divided by 3 remainder is 1
print(10 % 3)

# create a number in a variable
my_num = 5
print(my_num)

# convert a number to a string
print(str(my_num))

# using numbers with a string without errors
# convert a number to a string
print(str(my_num) + " is my favorite number")

# absolute value of a number
my_number = -17
print(abs(my_number))

# power of a number
# 3 ^ 2
print(pow(3, 2))

# getting the higher number returned
print(max(8, 6))

# getting the lower number returned
print(min(8, 6))

# rounding a number
print(round(8.6))

# importing functions
from math import *

# decimal rounded to the lower number
print(floor(8.6))

# decimal rounded to the upper number
print(ceil(8.6))

# square root of a number
print(sqrt(36))


# getting input from users
input("Enter your name: ")

# storing input to a variable
name = input("Enter your name: ")
user_age = input("Enter your age: ")
print("Hello " + name + "! You are " + user_age)

# basic calculator

num1 = input("enter a number")
num2 = input("enter another number")
result = float(num1) + float(num2)
print(result)

# lists in python are arrays in javascript
friends = ["Jess", "Jess", "Jess", "Hope", "Lexi", "Tattoo Girl"]

# lists can hold stings numbers and booleans
friends2 = ["Jess", 1, True]

# index starts at 0 just like javascript
print(friends[0])

# targeting index by negative numbers
# starts at the last index of list
# returnsTattoo Girl
print(friends[-1])

# accessing portions of a list
# this will return index of 1 and the rest of the list
print(friends[1:])

# accessing a range of items in a list
# returns names from index 1 and two stops at 3 not returning it
print(friends[1:3])

# modify an item in A list
friends[1] = "Hopey"
print(friends)

# LIST FUNCTIONS
lucky_numbers = [4, 8, 15, 42, 16, 23]

# extending a list
# this will combine 2 lists into 1
# friends.extend(lucky_numbers)
# print(friends)

# adding an item to the end of a list
friends.append("Dad")
print(friends)

# inserting an item to a list
# takes 2 parameters index to insert item and item
friends.insert(1, "Kelly")
print(friends)

# remove item from list
friends.remove("Kelly")

print(friends)

# deleting last item in list
friends.pop()
print(friends)

# finding the index of an ittem in a list
print(friends.index("Jess"))

# how many multiples of a item are in a list
print(friends.count("Jess"))

# sorting a list from acending to decending or alphabetically
friends.sort()
print(friends)

# sorting a list from acending to decending or alphabetically
lucky_numbers.sort()
print(lucky_numbers)

# reversing the order of a list
lucky_numbers.reverse()
print(lucky_numbers)

# copying a list
new_friends = friends.copy()
print(new_friends)

# to delete an entire list
friends.clear()
print(friends)
















