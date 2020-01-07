#Check whether integer is odd or even.
#Exercise 2
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#If the number is a multiple of 4, print out a different message.

#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

n = int(input("Enter an integer - "))

if n%2 == 0:
    if n % 4 == 0:
        print("Integer entered is even and a multiple of 4.")
    else:
        print ("Integer entered is even.")
else:
    print ("Integer entered is odd.")

num = int(input("Enter any integer as 'num' = "))
check = int(input("Enter any integer as 'check' = "))

if num%check == 0:
    print (str(num) + " can be divided evenly into " + str(check))
else:
    x = num/check
    print (str(num) + " when divided by " + str(check) + " gives remainder " + str(x))

    


