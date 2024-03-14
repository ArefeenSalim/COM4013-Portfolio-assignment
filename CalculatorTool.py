# this is a Calculator tool which can perform mathematical operations like addition, subtraction, multiplication, division, modulus, factorial and exponents-square and cube
# this calculator has been programmed using concepts like functions, loops and conditional statements.
print ("This is a Calculator")
print ("These are the operations")
# the list of mathematical operations 
print ("1 Addition +")
print ("2 Subtraction -")
print ("3 Multiplication *")
print ("4 Division /")
print ("5 Modulus %")
print ("6 Factorial !")
print ("7 Exponents ^ (Squared/cubed)")



def get_integer(prompt):
    # this function ensures that the user inputs the right type of input which is an integer here
    # it uses recursion to handle inputs and ensures type of input it valid or not
    value = input(prompt) 
    if value.lstrip('-').isdigit() or value.isdigit():
        return int(value)
    else:
        print("Invalid input! Only integers are allowed.")
        return get_integer(prompt)



def Addition():
    # this function adds two integers
    # assigning variables to user inputs
    n1= get_integer("enter the first number:")
    n2= get_integer("enter the second number:")
    sum = n1 + n2 # assigned a variable to store the sum of the integers
    print ("Sum of", n1, "and", n2, "is", sum) # the stored integers are then presented using their variable names



def Subtraction():
    # this function calculates the difference between two integers
    # assigning variables to user inputs
    n1= get_integer("enter the first number:")
    n2= get_integer("enter the second number:")
    difference = n1 - n2 # assigned a variable to store the difference of the integers
    print (f"The difference of {n1} and {n2} is {difference}") # the stored integers are then presented using their variable names



def Multiplication():
    # this function multiplies two integers and presents its product 
    n1= get_integer("enter the first number:")
    n2= get_integer("enter the second number:")
    product = n1 * n2 # assigned a variable to store the product of the integers
    print (f"The result of multiplying {n1} and {n2} is {product}") # the stored integers are then presented using their variable names



def Division():
    # this function divides two integers and presents its quotient and remainder
    n1= get_integer("enter the dividend:")
    while True: # The division operation is within a while loop to continuously prompt for the divisor until a non-zero integer has been inputted.
        n2= get_integer("enter the divisor:") 
        if n2 == 0: # this prevents division by zero errors.
            print("Division by zero is not allowed as it is a Math error.")
        else:
            quotient = n1 // n2 # (//) operator is used to obtain the quotient and has been stored in a variable.
            remainder = n1 % n2 # (%) operator is used to find the remainder and has been stored in a variable.
            print(f"Quotient: {quotient}")
            print(f"Remainder: {remainder}")
            # both the integers in the variables will be presented.
            break



def Modulus():
    # this function calculates the modulus or remainder of division between two integers.
    n1= get_integer("enter the dividend:")
    while True: # The division operation is within a while loop to continuously prompt for the divisor until a non-zero integer has been inputted.
        n2= get_integer("enter the divisor:")
        if n2 == 0: # this prevents division by zero errors.
            print("Error: Division by zero is not allowed.")
        else:
            remainder = n1 % n2 # (%) operator is used to find the remainder and has been stored in a variable.
            print(f"The result of {n1} % {n2} is: {remainder}")
            # the remainder stored in the variable will be presented
            break



def Factorial():
    # this function calculates the factorial of an integer
    # it illustrates the use of loops and if-else conditions to solve a problem.
    while True:
        n = get_integer("Enter a non-negative integer:")
        if n < 0: # calculates the factorial of a given non-negative integer only otherwise will ask user for another input.
            print("Invalid please enter a non-negative integer.")
        else:
            if n == 0 or n == 1:
                factorial = 1
            else:
                factorial = 1
                # this uses a for loop to accumalate the results
                for i in range(2, n + 1):
                    factorial *= i
            print(f"The factorial of {n} is {factorial}")
            break



def SquaredExponent():
    # this function calculates the square of an integer.
    # it makes use of the exponent operator to raise the number to the power of three
    while True:
        n = get_integer("enter your number:")
        if n == 0:
            print ("the square of 0 is 0")
            break
        else:
            sq = n ** 2 # this variable stores the squared number
            print (f"the square of {n} is {sq}")
            break



def CubedExponent():
    # this function determines the cube of an integer.
    # it makes use of the exponent operator to raise the number to the power of three
    while True:
        n = get_integer("enter your number:")
        if n == 0:
            print ("the cube of 0 is 0")
            break
        else:
            cube = n ** 3 # this variable stores the cubed number
            print (f"the cube of {n} is {cube}")
            break



def Calculator():
    # this is the main loop and calculator function control of the program
    # allows user to choose their options and directs them to the respective operation
    while True:
        toolChoice= input ("Enter the number corresponding to the operation")
        if toolChoice == "1":
            print ("1 Addition +")
            Addition()
            break
        elif toolChoice == "2":
            print ("2 Subtraction -")
            Subtraction()
            break
        elif toolChoice == "3":
            print ("3 Multiplication *")
            Multiplication()
            break
        elif toolChoice == "4":
            print ("4 Division /")
            Division()
            break
        elif toolChoice == "5":
            print ("5 Modulus %")
            Modulus()
            break
        elif toolChoice == "6":
            print ("6 Factorial !")
            Factorial()
            break
        elif toolChoice == "7":
            print ("7 Exponents ^ (Squared/cubed)")
            while True:
                # internal loop allowing the user to choose what kind of exponential operation they want to use and directs to the respective operation
                exponenentChoice= input("enter 2 for squaring, enter 3 for cubing")
                if exponenentChoice == "2":
                    print ("^2 squaring")
                    SquaredExponent()
                    break
                elif exponenentChoice == "3":
                    print ("^3 cubing")
                    CubedExponent()
                    break
                else:
                    print ("Invalid input, please input 2 for squaring and 3 for cubing")
            break
        else:
            print ("Invalid input, try again")


def main():
    # the use of a while loop in this function allows for repeated calculations without restarting the program.
    # this provides a user firendly interface for easy multiple calculations
    continueCalc = True
    while continueCalc:
        Calculator()
        doMore= input ("Do you want to calculate agin? (yes)")
        if doMore.lower() == "yes":
            print ("great!")
        else:
            print ("Thanks!Bye")
            continueCalc = False
            #The loop continues until the user exits, demonstrating the use of boolean flags to control the flow of the program.
main()
