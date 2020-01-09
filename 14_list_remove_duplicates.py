#Exercise 14
#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#Extras:
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.


def unique_list(a):
    b = [element for element in set(a)]
    return b

def unique_list_2(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b

a = [1,44,55,64,2,1,1,2,3,44,56,64,89,78,77,65,66,66,66,77,89]
print (a)
print (unique_list(a))
print (unique_list_2(a))


#  END  #