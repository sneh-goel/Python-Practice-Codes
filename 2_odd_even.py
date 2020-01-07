
num = int(input("Enter any integer as 'num' = "))
check = int(input("Enter any integer as 'check' = "))

if num%check == 0:
    print (str(num) + " can be divided evenly into " + str(check))
else:
    x = num/check
    print (str(num) + " when divided by " + str(check) + " gives remainder " + str(x))

#  END  #