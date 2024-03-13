print ("Choose your shape")
print ("1 Sqaure ")
print ("2 Triangle")
print ("3 Right Angled Triangle")
print ("4 Paralellogram")
print ("5 Rectangle")
print ("6 Rhombus")
print ("7 V")
print ("8 Hourglass")


def Square():
    n = int(input("Enter the size of the square: "))
    for i in range(n):
        print("* "*n)
    print(f"Area: {n*n}")    

def Triangle():
    n = int(input("Enter the height of the triangle: "))
    b = int(input("Enter the base of triangle: "))
    for i in range(1, n+1):
        print(" "* (n - i) + "* " * i)
    print(f"Area: {(b * n) / 2}")

def RightAngledTriangle():
    n = int(input("Enter the height of the right angled triangle: "))
    b = int(input("Enter the base length of the right angled triangle: "))
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print()
    print(f"Area: {(b * n) / 2}")

def Paralellogram():
    n = int(input("Enter the height of the paralellogram: "))
    m = int(input("Enter the length of the base: "))
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(m):
            print("* ", end="")
        print() 
    print(f"Area: {n * m}")

def Rectangle():
    h = int(input("Enter the height of the rectangle: "))
    b = int(input("Enter the length of the base: "))
    for i in range(h):
        for j in range(b):
            print("* ", end="")
        print()
    print(f"Area: {h * b}")

def Rhombus():
   n = int(input("Enter the length of the side of a rhombus: ")) 
   for i in range(1, n + 1):
       print(" " * (n - i) + "* " * i)
   for i in range(n - 1, 0, -1):
       print(" " * (n - i) + "* " * i)

def V():
    h = int(input("Enter the height of the 'v': "))
    for i in range(h):
        for j in range(i):
            print(" ", end="")
        print("**", end="")
        middle_space = 2 * (h - i) - 3
        for k in range(middle_space):
            print(" ", end="")
        if i != h - 1:
            print("**", end="")
        print()

def Hourglass():
    length = int(input("Enter the length of the top/bottom of the hourglass: "))
    for i in range(length, 0, -1):
        print((' ' * (length - i) + '*' * (2 * i - 1)).center(2 * length - 1))
    for i in range(1, length + 1):
        print((' ' * (length - i) + '*' * (2 * i - 1)).center(2 * length - 1))



def Shape():
    while True:
        shape = input ("Enter the number of the shape: ")
        if shape == "1":
            print (" 1 Square")
            Square()
            break
        elif shape == "2":
            print("2 Triangle")
            Triangle()
            break
        elif shape== "3":
            print("3 Right Angled Triangle")
            RightAngledTriangle()
            break
        elif shape == "4":
            print("4 Paralellogram")
            Paralellogram()
            break
        elif shape == "5":
            print("5 Rectangle")
            Rectangle()
            break
        elif shape == "6":
            print("6 Rhombus")
            Rhombus()
            break
        elif shape == "7":
            print("7 V")
            V()
            break
        elif shape == "8":
            print("8 Hourglass")
            Hourglass()
            break
        else: 
            print ("invalid choice")

def main():
    Shape()
main()    
