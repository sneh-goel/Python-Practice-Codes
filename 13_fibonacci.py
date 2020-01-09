#Exercise 13
#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum
# of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibo(n):
    a = 0
    b = 1
    c = 1
    fib = [1]
    while n >= 0:
        fib.append(c)
        a = b
        b = c
        c = a+b
        n -= 1
    return fib

n = int(input("How many Fibonacci numbers to be generated - "))
print (fibo(n))

#  END  #