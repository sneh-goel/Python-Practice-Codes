#Character Input

name = input("What is your name dear user? \n")
age = int(input("If I may also know your age dearest user? \n"))

year = 2020 + (100 - age)
year = str(year)

print ("My user your name is",name, "and you age is",age, ".")

result =name + ', you will turn 100 years old in ' + year + '.' + '\nHave fun while it lasts. \n:)'

print (result)

n = int(input("\n\nPlease enter an integer from 1 - 10.\n"))

while n>=0:
    print (result)
    n = n - 1

