#Exercise 15
#Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

def reverse_string(s):
    x = s.split()
    return (" ".join(x[::-1]))

s = input("Enter any sentence with multiple words - ")
print (reverse_string(s))


#   END   #