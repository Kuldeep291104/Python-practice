#q1 program to write multiplication table of a given number of loop
'''n=int(input("enter your number"))

for i in range(1,11):
    print(f"{n} * {i}= {n*i}")

'''
'''n=int(input("eneter your number"))
for i in range(1,11):
    print(f"{n}*{i}={i*n}")
    i +=1'''
#q2 write a program to greet the names in a list whose initials are starting withS

'''names=["kuldeep","Sharon","rashi","Shameena","shanu","abhay"]
for i in names:
    if(i.startswith ("S")):
        print(f"hello {i}")
    
'''

# using while loop to print multiplication of table
'''a=int(input("enter a number"))
i=1
while(i<11):
        print(f"{a}*{i}={i*a}")
        i+=1
        '''
#write a program to find a number is prime or not
'''n=int(input("enter a number"))

for i in range(2,n):
    if(n%i) ==0:
        print("not prime")
        break
    else:
        print("prime")'''
#print a start pattern

'''n=int(input("enter a number"))

for i in range(1,n+1):

    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")'''
#printing a star pattern2

'''n=int(input("enter a number"))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")


'''

'''n=int(input("enter a number"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")'''

#reverse table
'''n=int(input("enter a number"))

for i in range(1,11):
    print(f"{n}*{11-i}={n*(11-i)}")

          '''

