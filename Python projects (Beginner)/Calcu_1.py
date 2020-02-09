#Calculator prototype 1
#This program can calculate the result of 2 numbers only
#This is the first protoyype, with time this should get better and improve to unlimited numbers
#Now, lets begin:
#Since this is a first prototype, I will not be using functions
Final = 0

#First, let's ask the user for an input of the first number
num1 = int(input("Enter the first number: "))

#Now we will ask them for the operation the want to preform
#Note: If the operation entered is not valid, then it will keep asking the person to input another operation
opr = input("What would you like to do? (x or - or + or /)")
while opr != "x" and opr != "-" and opr != "/" and opr != "+":
    print("This is not a valid operation.")
    opr = input("What would you like to do? (x or - or + or /)")

#Ask for 2nd number
num2 = int(input("Enter the second number: "))

#Now we shall use IF statements to decide what to do with these numbers
if opr == "x":
    Final = num1 * num2
elif opr == "-":
    Final = num1 - num2
elif opr == "+":
    Final = num1 + num2
elif opr == "/":
    Final = num1 / num2
    
#This will print the final answer
print("The final answer is: " + str(Final))