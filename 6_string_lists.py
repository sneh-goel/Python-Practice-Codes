#Exercise 6
#Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

s = input('Enter any word - ')

p = []
q = []

x = 0
while x < len(s):
    p.append(s[x])
    x = x + 1

y = len(s) - 1
while y >= 0:
    q.append(s[y])
    y = y - 1

print (q)
print (p)

if p == q:
    print ("Entered string is a Palindrome.")
else:
    print ("Entered string is not a Palindrome.")
