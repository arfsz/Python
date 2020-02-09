#Welcome to calculator prototype 2!
#This time its a bit less complicated
#The reason for this is cause I will be using functions
#If you feel that there is a need to improve, please do say so
#Anyways lets begin:

#First we will be making the main functions for the operations
#It is important to remember that if you want to PRINT a function you must add a return value,
#Otherwise, it will simply print "None"
def multi():
    return num1 * num2

def divi():
    return num1 / num2

def add():
    return num1 + num2

def sub():
    return num1 - num2
#As you may notice, these may not be very complex, but they help us make the code easier to read and
#easier to use
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
#This time instead of using the direct calculations, we will refer back to our functions
if opr == "x": 
    Final = multi()
elif opr == "-":
    Final = sub()
elif opr == "+":
    Final = add()
elif opr == "/":
    Final = divi()
    
#This will print the final answer
print("The final answer is: " + str(Final))
