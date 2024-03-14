print ("This is a Calculator")
print ("These are the operations")
print ("1 Addition +")
print ("2 Subtraction -")
print ("3 Multiplication *")
print ("4 Division /")
print ("5 Modulus %")
print ("6 Factorial !")
print ("7 Exponents ^ (Squared/cubed)")

def get_integer(prompt):
    value = input(prompt)
    if value.lstrip('-').isdigit() or value.isdigit():
        return int(value)
    else:
        print("Invalid input! Only integers are allowed.")
        return get_integer(prompt)



def Addition():
    n1= get_integer("enter the first number:")
    n2= get_integer("enter the second number:")
    sum = n1 + n2
    print ("Sum of", n1, "and", n2, "is", sum)



def Subtraction():
    n1= get_integer("enter the first number:")
    n2= get_integer("enter the second number:")
    difference = n1 - n2
    print (f"The difference of {n1} and {n2} is {difference}")



def Multiplication():
    n1= get_integer("enter the first number:")
    n2= get_integer("enter the second number:")
    product = n1 * n2
    print (f"The result of multiplying {n1} and {n2} is {product}")



def Division():
    n1= get_integer("enter the dividend:")
    while True:
        n2= get_integer("enter the divisor:")
        if n2 == 0:
            print("Division by zero is not allowed as it is a Math error.")
        else:
            quotient = n1 // n2
            remainder = n1 % n2
            print(f"Quotient: {quotient}")
            print(f"Remainder: {remainder}")
            break



def Modulus():
    n1= get_integer("enter the dividend:")
    while True:
        n2= get_integer("enter the divisor:")
        if n2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            remainder = n1 % n2
            print(f"The result of {n1} % {n2} is: {remainder}")
            break



def Factorial():
    while True:
        n = get_integer("Enter a non-negative integer:")
        if n < 0:
            print("Invalid please enter a non-negative integer.")
        else:
            if n == 0 or n == 1:
                factorial = 1
            else:
                factorial = 1
                for i in range(2, n + 1):
                    factorial *= i
            print(f"The factorial of {n} is {factorial}")
            break



def SquaredExponent():
    while True:
        n = get_integer("enter your number:")
        if n == 0:
            print ("the square of 0 is 0")
            break
        else:
            sq = n ** 2
            print (f"the square of {n} is {sq}")
            break



def CubedExponent():
    while True:
        n = get_integer("enter your number:")
        if n == 0:
            print ("the cube of 0 is 0")
            break
        else:
            cube = n ** 3
            print (f"the cube of {n} is {cube}")
            break



def Calculator():
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
    continueCalc = True
    while continueCalc:
        Calculator()
        doMore= input ("Do you want to calculate agin? (yes)")
        if doMore.lower() == "yes":
            print ("great!")
        else:
            print ("Thanks!Bye")
            continueCalc = False
main()


if __name__ == "__main__":
    main()