# this is a shape generator which makes shapes using user input and provides the user with the area and allows them to choose if they want the shape to be outlined or filled
# the user can select from a variety of shapes to generate, including a square, equilateral triangle, right-angled triangle, parallelogram, rectangle, and hourglass.
print ("This is a shape generator")
print ("Choose your shape")
print ("1 Sqaure ")
print ("2 Equilateral Triangle")
print ("3 Right Angled Triangle")
print ("4 Paralellogram")
print ("5 Rectangle")
print ("6 Hourglass")

def get_integer(prompt):
    # function to get a positive integer from the user, with input validation to ensure the input is a digit
    user_input = input(prompt)
    while not user_input.isdigit():
        user_input = input("Invalid input. Please enter a positive number: ")
    return int(user_input)



def Square():
    # the Square function implements an algorithm to generate a square, with the option to display an outlined or filled square.
    # the area is calculated and displayed, showing the application of geometric principles in programming.
    n = get_integer("Enter the size of the square: ")
    outline = input("Do you want the shape outlined? (yes or no): ").lower()
    if outline == "yes":
        # a loop is used here to print each row of the square pattern.
        for i in range(n): # the range(n) generates a sequence from 0 to n-1, which corresponds to the rows of the square.
            # the first and last iterations create the top and bottom borders of the square.
            if i == 0 or i == n - 1:
                print("* " * n) # rrints a line of n number of asterisks without spaces which creates a solid line.
            else:
                # For rows other than the first and last it prints a border with a space-filled inside.
                print("* " + "  " * (n - 2) + "*") # constructs a string with an asterisk at the beginning and end
                # n-2 spaces in between to form the sides of the square with an empty inside.
    else:
        # loop is used to print each row of a filled square.
        for i in range(n):
            print("* " * n) # this prints a solid line of n number of asterisks which are repeated n number of times to create a filled square.
    print(f"Area: {n * n}") # the function prints the area of the square



def EquilateralTriangle():
    # ask the user to input the height of the triangle.
    n = get_integer("Enter the height of the triangle: ")
    outline = input("Do you want the shape outlined? (yes or no): ").lower()
    if outline == "yes": 
        # loop through the number of lines equal to the height of the triangle.
        for i in range(1, n+1):
            # if it's the first or the last line print the base.
            if i == 1 or i == n:
                print(" " * (n - i) + "* " * i)
            else: # print the outline with spaces between the stars
                print(" " * (n - i) + "*" + " " * (2*i - 3) + "*")
    else:
        # loop through the number of lines equal to the height of the triangle.
        for i in range(1, n+1):
            # print a row of the triangle with proper spacing and stars.
            print(" " * (n - i) + "* " * i)
    print(f"Area: {(n * n) / 2}") # the function prints the area of the equilateral triangle



def RightAngledTriangle():
    # ask the user to input the height and base of the triangle.
    n = get_integer("Enter the height of the right angled triangle: ")
    b = get_integer("Enter the base length of the right angled triangle: ")
    outline = input("Do you want to see the outline? (yes or no): ").lower()

    for i in range(n):
        if outline == 'yes':
            if i == 0 or i == n - 1:
                print('* ' * (i + 1))
            else:
                print('*' + ' ' * (2 * i - 1) + '*')
        else:
            print('* ' * (i + 1)) # prints a filled triangle by printing a line of asterisks.
    print(f"Area: {(b * n) / 2}") # the function prints the area of the right angled triangle



def Parallelogram():
    # ask the user height and base of the paralellogram
    n = get_integer("Enter the height of the parallelogram: ")
    m = get_integer("Enter the length of the base: ")
    outline = input("Do you want to see the outline only (yes or no)? ").lower()
    for i in range(n): # for loop to iterate over the height of the parallelogram
        print(" " * (n - i - 1), end="")
        # for loop to iterate over the length of the base of the parallelogram.
        for j in range(m):
            if outline == "yes":
                # check if the current position is on the border of the parallelogram.
                if j == 0 or j == m - 1 or i == 0 or i == n - 1:
                    print("* ", end="") # print astrix for the border
                else:
                    print("  ", end="") # print a space for the internal area of the parallelogram.
            else:
                print("* ", end="") # print astrix to fill the shape.
         # print a newline after each row.
        print() 
    print(f"Area: {n * m}")# the function prints the area of the parallelogram

    

def Rectangle():
    # ask the user height and base of the rectangle
    h = get_integer("Enter the height of the rectangle: ")
    b = get_integer("Enter the length of the base: ")
    outline = input("Do you want to see the outline only (yes or no)? ").lower()
    for i in range(h): # a loop that will run h number of times where h is the height of the rectangle.
        if outline == "yes" and i != 0 and i != h - 1: 
            print('*' + ' ' * (b - 2) + '*') # print the horizontal sides of the rectangle.
        else: 
            print('*' * b) # printing a full line of asterisks
    print(f"Area: {h * b}") # the function prints the area of the rectangle



def Hourglass():
    # this loop continues to prompt the user until an even number is entered
    while True:
        n = get_integer("Enter the height of the shape: ")
        if n % 2 == 0: # checks if the number is even
            break #exits the loop if the number is even
        else:
            print("Please input an even number as the height") 
    n2 = n // 2 # divides the height by 2 to work with the top and bottom halves of the hourglass
    b = n2 #  tores half the height into variable b as it will be the base of the shape, done to make it convinient to understand the code
    outline = input("Do you want to see the outline only (yes or no)? ").lower()
    if outline == "yes":
        # prints the top half of the outline of the hourglass
        print("* " * n2) # prints the top line of asterisks
        for i in range(n2 - 1, 0, -1): # counts down from n2-1 to 1
            # prints spaces and then asterisks to form the outline
            print(" " * (n2 - i) + "*" + " " * (2 * i - 3) + ("*" if i > 1 else ""))
        # prints the bottom half of the outline of the hourglass
        for i in range(2, n2):
            # prints spaces and then asterisks to form the outline
            print(" " * (n2 - i) + "*" + " " * (2 * i - 3) + "*")
        print("* " * n2) # prints the bottom line of asterisks
    else: 
        # prints the top half of the filled hourglass
        for i in range(n2, 0, -1): # counts down from n2 to 1
            # prints the full line of asterisks
            print(" " * (n2 - i) + "* " * i)
        # prints the bottom half of the filled hourglass
        for i in range(1, n2 + 1): # counts up from 1 to n2
            # prints the full line of asterisks
            print(" " * (n2 - i) + "* " * i)
    print(f"Area: {(b * n2)*2}") # prints the area of the hourglass shape



def Shape():
    while True:
        # this is the main loop and function control of the program
        # allows user to choose their options and directs them to the respective shape generator
        shape = input ("Enter the number of the shape: ")
        if shape == "1":
            print (" 1 Square")
            Square()
            break
        elif shape == "2":
            print("2 Triangle")
            EquilateralTriangle()
            break
        elif shape== "3":
            print("3 Right Angled Triangle")
            RightAngledTriangle()
            break
        elif shape == "4":
            print("4 Paralellogram")
            Parallelogram()
            break
        elif shape == "5":
            print("5 Rectangle")
            Rectangle()
            break
        elif shape == "6":
            print("6 Hourglass")
            Hourglass()
            break
        else: 
            print ("invalid choice")

def main():
    # the use of a while loop in this function allows for repeated trials without restarting the program.
    continueShape = True
    while continueShape:
        Shape()
        doMore= input ("Do you want to draw more shapes? (type (yes) if you want to draw more shapes or press enter to exit)")
        if doMore.lower() == "yes":
            print ("great!")
        else:
            print ("Thanks!Bye")
            continueShape = False
            #The loop continues until the user exits, demonstrating the use of boolean flags to control the flow of the program.
main()    

