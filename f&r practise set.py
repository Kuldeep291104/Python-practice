#1 Write a program to find the greatest number among the 3.
'''a=int(input("enter a number")) 
b=int(input("enter a number")) 
c=int(input("enter a number")) 
def greatest(a,b,c):
    if(a>b and a>c):
        print(f"the greatest number is {a}")
    
    elif(b>a and b>c):
        print(f"the greatest number is {b}")

    elif(c>a and c>b):
        print(f"the greatest number is {c}")

greatest(a,b,c)'''

#2 Write a python program using function to covert celcius into farenheit
'''def f_to_c(f):

    return((5/9)*(f-32))

f=int(input("Enter the temperature in celcius"))
        
print(f_to_c(f))''' 


#3 How do you prevent a python print() function to print a new line at the end

'''print("a")
print("b")
print("c", end="")
print("d", end="")'''

#using an end() function 

#4write a recursive function to calculate the sum of first natural n numbers.

'''def sum(n):
    if n==1:
        return 1
    else:
        return sum(n-1)+n
a=int(input ("Enter the number whose add up sum you need"))

print(f"{sum(a)} is the sum of your number {a}")'''

#write a python program to print first n lines of the following pattern
'''
***
**          for n =3
*   

'''

'''def pattern(n):
    if(n==0):
        return 
        
    print("*"*n)
    pattern(n-1)
print(pattern(3))


def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)


(pattern(4))'''

#Write a program to convert inches to cm

'''def convert(n):
        return(n*2.5)

n=int(input("enter a number"))
print((convert(n)))'''\


#Write a python program to remove a given word from a list and strip it at the same time


'''def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["kuldeep","rohan","abhay","an"]

print(rem(l,"an"))'''



#multiplication table


def tb(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
    return
n=int(input("enter a number"))
print(tb(n))

