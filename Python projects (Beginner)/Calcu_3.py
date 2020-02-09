#Welcome to the 3rd Calculator prototype!
#This time its more complex, we will have an infinite amount of operations until
#the user decides to stop them.
#This program will use the functions previously created in the "calc_functions" file, however to
#Make it easier to type, we will change it to cf.
from Cf import multi, divi, add, sub

print ("Hello. This is a calculator.")

x = 1
result = 0

while x == True:
    a = int(input("Enter a number: "))
    o = input("Choose the operator (*, /, +, -): ")
    
    while o != "+" and o != "*" and o != "/" and o != "-":
        print ("Invalid Operation, Please try again")
        o = input("Choose the operator (*, /, +, -): ")
    
    b = int(input("Enter another number: "))
    
    if o == "*": 
        f = multi(a , b)
    elif o == "-":
        f = sub(a , b)
    elif o == "+":
        f = add(a , b)
    elif o == "/":
        f = divi(a , b)
    
    result = result + f
    
    print ("Current answer: " + str(result))
    
    equal = input("End? (y/n): ")
    if equal == "y":
        break

answer = result

print ("Final answer is: " + str(answer))
    
    
    