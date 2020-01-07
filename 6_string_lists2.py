#Exercise 6
#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

word = input("Enter any word - ")
reverse = word[::-1]
print (reverse)
if word == reverse:
    print ("Entered word is Palindrome.")
else:
    print ("It is not a Palindrome.")