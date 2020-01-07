#Exercise 3
#Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

#Extras:
#Instead of printing the elements one by one, make a new list that has all the elements
#less than 5 from this list in it and print out this new list.
#
#Ask the user for a number and return a list that contains only elements from the original
#list a that are smaller than that number given by the user.

def list_compare (list, compare_no, new_list):
    for element in list:
        if element < compare_no:
            new_list.append(element)

x = [1,1,2,3,5,8,13,21,34,55,89]
y = []

print ("Given List is:")
print (x)

list_compare(x, 5, y)
print ("\nList of elements in the given list less than 5 are :")
print (y)

p = int(input('\nEnter an integer to compare list elements: '))
list_compare(x, p, y)
print ("\nList of elements in the given list less than " + str(p) + " are : ")
print (y)

#  END  #