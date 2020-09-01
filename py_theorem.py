print('''

            ██████╗ ██╗   ██╗    ████████╗██╗  ██╗███████╗ ██████╗ ██████╗ ███████╗███╗   ███╗
           v██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██║  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝████╗ ████║
            ██████╔╝ ╚████╔╝        ██║   ███████║█████╗  ██║   ██║██████╔╝█████╗  ██╔████╔██║
            ██╔═══╝   ╚██╔╝         ██║   ██╔══██║██╔══╝  ██║   ██║██╔══██╗██╔══╝  ██║╚██╔╝██║
            ██║        ██║          ██║   ██║  ██║███████╗╚██████╔╝██║  ██║███████╗██║ ╚═╝ ██║
            ╚═╝        ╚═╝          ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝
                                                                                               \n ''')


print ('\n***********************************************************************************\n')






#Pythagoras Theorm

# c=√a²+b²
# a=√c²-b²
# b=√c²-a²


print ('''Usage:•1• Enter side name which you want to find.Like- Hypotenuse,Perpendicular,Base.Remember first letter should be capital 
•2• Then enter the two given side. ''')


print ("\nEnter The Side Name-\n")
x = input()

if x== "Hypotenuse":
    print ("\nSolving For-\n")
    print (x)
    print ("\nEnter Perpendicular Side=\n")
    a = float(input())
    print (a)
    print ("\nEnter Base side\n")
    b = float(input())
    print (b)
    c=((a**2)+(b**2))
    print ("\n Hypotenuse =\n")
    print (c**(1/2))


if x== "Perpendicular":
    print ("\nSolving For-\n")
    print (x)
    print ("\nEnter Hypotenuse Side=\n")
    a = float(input())
    print (a)
    print ("\nEnter Base side\n")
    b = float(input())
    print (b)
    d=((a**2)-(b**2))
    if a<b:
        print ("Error Hypotenuse cannot be less than Base")
    if a>b:
        print ("\nPerpendicular =\n")
        print (d**(1/2))     
              

if x== "Base":
    print ("\nSolving For-\n")
    print (x)
    print ("\nEnter Hypotenuse Side=\n")
    a = float(input())
    print (a)
    print ("\nEnter Perpendicular side\n")
    b = float(input())
    print (b)
    e=((a**2)-(b**2))
    if a<b:
        print ("\nError Hypotenuse cannot be less than Perpendicular")
    
    if a>b:
        print ("\n Base =\n")
        print (e**(1/2))    
    
else:
    print ("\nError invalid choice\n")
