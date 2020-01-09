# Exercise 12
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

def first_and_last(a):
    b = []
    b.append(a[0])
    b.append(a[len(a) - 1])
    return b

import random

n = int(input("Enter the no. of integers in the list -  "))
x = random.sample(range(1,50),n)

print ("List is -", x)
print ("First and last elements are - ", first_and_last(x))


#   END   #