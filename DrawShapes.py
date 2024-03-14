print ("Choose your shape")
print ("1 Sqaure ")
print ("2 Triangle")
print ("3 Right Angled Triangle")
print ("4 Paralellogram")
print ("5 Rectangle")
print ("6 Hourglass")

#################################################################################################

def Square():
    n = int(input("Enter the size of the square: "))
    outline = input("Do you want the shape outlined? (yes or no): ").lower()
    if outline == "yes":
        for i in range(n):
            if i == 0 or i == n - 1:
                print("* " * n)
            else:
                print("* " + "  " * (n - 2) + "*")
    else:
        for i in range(n):
            print("* " * n)
    print(f"Area: {n * n}")

##################################################################################################

def EquilateralTriangle():
    n = int(input("Enter the height of the triangle: "))
    outline = input("Do you want the shape outlined? (yes or no): ").lower()
    if outline == "yes": 
        for i in range(1, n+1):
            if i == 1 or i == n:
                print(" " * (n - i) + "* " * i)
            else:
                print(" " * (n - i) + "*" + " " * (2*i - 3) + "*")
    else:
        for i in range(1, n+1):
            print(" " * (n - i) + "* " * i)
    print(f"Area: {(n * n) / 2}")

##################################################################################################

def RightAngledTriangle():
    n = int(input("Enter the height of the right angled triangle: "))
    b = int(input("Enter the base length of the right angled triangle: "))
    outline = input("Do you want to see the outline? (yes or no): ").lower()

    for i in range(n):
        if outline == 'yes':
            if i == 0 or i == n - 1:
                print('* ' * (i + 1))
            else:
                print('*' + ' ' * (2 * i - 1) + '*')
        else:
            print('* ' * (i + 1))
    print(f"Area: {(b * n) / 2}")

##################################################################################################

def Parallelogram():
    n = int(input("Enter the height of the parallelogram: "))
    m = int(input("Enter the length of the base: "))
    outline = input("Do you want to see the outline only (yes or no)? ").lower()
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(m):
            if outline == "yes":
                if j == 0 or j == m - 1 or i == 0 or i == n - 1:
                    print("* ", end="")
                else:
                    print("  ", end="")
            else:
                print("* ", end="")
        print() 
    print(f"Area: {n * m}")

##################################################################################################    

def Rectangle():
    h = int(input("Enter the height of the rectangle: "))
    b = int(input("Enter the length of the base: "))
    outline = input("Do you want to see the outline only (yes or no)? ").lower()
    for i in range(h):
        if outline == "yes" and i != 0 and i != h - 1: 
            print('*' + ' ' * (b - 2) + '*')
        else: 
            print('*' * b)
    print(f"Area: {h * b}")

##################################################################################################

def Hourglass():
    while True:
        n = int(input("Enter the height of the shape: "))
        if n % 2 == 0:
            break 
        else:
            print("Please input an even number as the height") 
    n2 = n // 2
    b = n2 
    outline = input("Do you want to see the outline only (yes or no)? ").lower()
    if outline == "yes": 
        print("* " * n2)
        for i in range(n2 - 1, 0, -1):
            print(" " * (n2 - i) + "*" + " " * (2 * i - 3) + ("*" if i > 1 else ""))
        for i in range(2, n2):
            print(" " * (n2 - i) + "*" + " " * (2 * i - 3) + "*")
        print("* " * n2)
    else: 
        for i in range(n2, 0, -1):
            print(" " * (n2 - i) + "* " * i)
        for i in range(1, n2 + 1):
            print(" " * (n2 - i) + "* " * i)
    print(f"Area: {(b * n2)*2}")

##################################################################################################

def Shape():
    while True:
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
    while True:
        Shape()
        doMore= input ("Do you want to draw more shapes? (yes or no)")
        if doMore != "yes":
            print ("thanks for drawing shapes")
            break
main()    

if __name__ == "__main__":
    main()
