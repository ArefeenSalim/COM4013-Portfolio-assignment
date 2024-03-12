print ("Choose your shape")
print ("1 Sqaure ")
print ("2 Triangle")
print ("3 Right Angled Triangle")
print ("4 Paralellogram")
print ("5 Rectangle")
print ("6 ")
print ("7 ")
print ("8 ")


def Square():
    n = int(input("Enter the size of the square: "))
    for i in range(n):
        print("* "*n)

def Triangle():
    n = int(input("Enter the height of the triangle: "))
    for i in range(1, n + 1):
        print(" "* (n - i) + "* " * i)

def RightAngledTriangle():
    n = int(input("Enter the height of the right angled triangle: "))
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print()

def Paralellogram():
    n = int(input("Enter the height of the paralellogram: "))
    m = int(input("Enter the length of the base: "))
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(m):
            print("* ", end="")
        print() 

def Rectangle():
    n = int(input("Enter the height of the rectangle: "))
    m = int(input("Enter the length of the base: "))
    for i in range(n):
        for j in range(m):
            print("* ", end="")
        print()

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
        #elif shape == "6":
            #print("6")
            #break
        #elif shape == "7":
            #print("7")
            #break
        #elif shape == "8":
            #print("8")
            #break
        else: 
            print ("invalid choice")

def main():
    Shape()
main()    
