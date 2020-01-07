#Exercise 5
# #Take two lists, say for example these two:

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
# Randomly generate two lists to test this


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = []

for p in a:
    if p in b:
        if p not in x:
            x.append(p)

print ('List 1 = ')
print (a)
print ('List 2 = ')
print (b)

print('\n')
print(x)





