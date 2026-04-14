#1 Write a program to find the greatest number among the 3.
a=int(input("enter a number")) 
b=int(input("enter a number")) 
c=int(input("enter a number")) 
def greatest(a,b,c):
    if(a>b and a>c):
        print(f"{a}is the greatest")
    
    elif(b>a and b>c):
        print(f"{b} is greatest ")

    elif(c>a and c>b):
        print(f"{c} is the greatest")