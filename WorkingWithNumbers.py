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

# basic calculator

num1 = input("enter a number")
num2 = input("enter another number")
result = float(num1) + float(num2)
print(result)
