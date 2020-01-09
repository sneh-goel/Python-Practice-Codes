#Exercise 11 (and Solution)
#Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.


def divisors(x):
    a = 2
    list = []
    while a < x:
        if x%a == 0:
            list.append(a)
        a += 1
    return len(list)

num = int(input("Enter an integer - "))
no_of_divisors = divisors(num)

if num == 1:
    print ("Entered num is not prime.")
else:
    if no_of_divisors == 0:
        print ("Entered num " + str(num) + " is prime.")
    else:
        print ("Entered num is not prime.")


#  END  #