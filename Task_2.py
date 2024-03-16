#Codsoft Internship
# Task-2 Calculator
def add(num1,num2): # function perform addtion
    return num1+num2
def sub(num1,num2): # function perform subtraction
    return num1-num2
def multiply(num1,num2):# function perform Multiplication
    return num1*num2
def division(num1,num2):# function perform Division
    return num1-num2
def modulus(num1,num2):# function perform Modulus
    return num1%num2


num1=float(input('Enter num1:')) #get  a input from user
num2=float(input('Enter num2:')) #get  a input from user
print("1. + \n2. - \n3. *\n4. / \n5. %") 
option=input('Enter your option:')#get a option from user

if option=='+':
    print(add(num1,num2)) #add function call
elif option=='-':
    print(sub(num1,num2))#sub function call
elif option=='*':
    print(multiply(num1,num2))#multiply function call
elif option=='/':
    print(division(num1,num2))#division function call
elif option=='%':
    print(modulus(num1,num2))#modulus function call
else:
    print("...Enter valid option...") #print the statement if the input is Invalid

