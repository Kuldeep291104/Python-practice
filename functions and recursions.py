#Function Defination

'''def avg():
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    c=int(input("enter a number"))

    print((a+b+c)/3)




def gd():
    print("good day")'''

#there are 2 types of functions
"1.Built in functions"
 #print(),len(),range(),uppercase()

"2.User-defined functions"
 #avg() , gd()


#function with arguments 
'''
def goodday(name,ending="sure"):
    print("good day",name,ending)

goodday("kuldeep","hello")

'''

#Recursion

#factorial(1)=1
#factorial(2)=2*1
#factorial(3)=3*2*1
#factorial(4)=4*3*2*1
#factorial(5)=8*4*3*2*1

'''
def factorial(n):
    if (n==1):
        return 1
    
    return n * factorial(n-1)


n=int(input("enter a number:"))

print(f"The factorial of your provided number is:{factorial(n)}")'''



    