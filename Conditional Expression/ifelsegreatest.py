num1 = int (input("Enter the number 1 = "))
num2 = int (input("Enter the number 2 = "))
num3 = int (input("Enter the number 3 = "))
num4 = int (input("Enter the number 4 = "))
if (num1>num2):
    digit = num1
else:
    digit = num2
if (num3>num4):
    digit2 = num3
else:
    digit2 = num4
if (digit>digit2):
    print("The greatest number is = " + str(digit))
else:
    print("The geatest number is this = "+ str(digit2))  

 #---------------------------------------------------------------------------------------   

'''"The greatest number is this = " is a string literal that serves as the message to be printed.
----->> str(digit2) <-----converts the value of the variable digit2 into a string so that it can be concatenated
    ith the message.'''

