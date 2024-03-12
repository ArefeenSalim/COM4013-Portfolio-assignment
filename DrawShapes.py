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
    for i in range(0, n):
        for j in range(0, n): 
            print("*", end="")
    print()

def Triangle():

def Shape():
    while True:
        shape = input ("Enter the number of the shape")
        if shape == "1":
            print (" 1 Square")
            Square()
            break
        #elif shapeType== "2":
            #print("2 Triangle")
            #break
        #elif shapeType== "3":
            #print("3 Right Angled Triangle")
           # break
        #elif shapeType== "4":
           # print("4 Paralellogram")
            #break
        #elif shapeType== "5":
            #print("5 Rectangle")
            #break
        #elif shapeType== "6":
            #print("6")
            #break
        #elif shapeType== "7":
            #print("7")
            #break
        #elif shapeType== "8":
            #print("8")
            #break
        else: 
            print ("invalid choice")

def main():
    Shape()
    Square()
main()    
