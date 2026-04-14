'''print("hello,kuldeep")
x=6
y="hellowold"
print(x,y)
#this is a comment'''

#triple means a comment bigg
#below states how a variable is creeated and how a number can be framed
'''x=str(32)
y=int(3)
z=float(5)
print(x,y,z)'''



#now we will learn to print how to know if a integer is of what data type

#for example let's take x as 5 and print it

'''x=5
print(type(x))

a="hello kuldeep"
print(type(a))
'''
#this is how it is done

#there i this camel case in which an integer name except the start starts with a capital letter
#for example
'''myBigBrother="abhaysingh Rathod"
print(myBigBrother)'''

#now after camel case let's learn about the Pascal case where each variable name starts with a capital letter

#for example

'''MyBigBrother="abhaysingh rathod"
print(MyBigBrother)'''

#at last comes the third snake case where each and every letter starts with a small letter
#for example
'''mybigbrother="abhaysinghrathod"
print(mybigbrother)'''

#how to assign various values to a single variable

'''x,y,z= 23,"hello",66.33
print(type(x))
print(type(y))
print(type(z))'''

#one value to multiple variables

'''x=y=z="orange"
print(x)
print(y)
print(z)'''


#unpack a collection 


'''Fruits=['apple','banana','orange']
x,y,z=Fruits

print(x)
print(y)
print(z)
'''
#using a gloabal variable
'''x="my name is "

def name():
    print(x,"kuldeep")
    print(x,"abhay")

def principal():
    print(x,"principal salma miss")

name()
principal()    
'''
#how to define a global variable inside a particular function 


'''def name():
    global x 
    x="my name is"

    print(x,"kuldeep")

def principal():
    print(x,"principal salma miss")

name()
principal()'''



#not defining a global x and a particaula x for every single function


'''def test():
    x="my marks are"
    print(x,"90")

def name():
    x="my name is"
    print(x,"kuldeep")

name()
test()   '''

#lets learn about data types and how they are written

#for list we use [] this bracket
#for tuple we use () this bracket
#for dictionary we use{} and also for set this bracket
#the main diffrence is that in dictionary we also specify the variable

'''alist=[23,45,66]
atuple=(23,43,55)
aset={23,44,45}
adict={"rollno":45,"name":"kuldeep","class":12}

print(type(aset))
print(type(alist))
print(type(atuple))
print(type(adict))'''

#bool type
'''x=True
print(type(x))'''


#TYPE COVERSION
'''x=23
y="23"
c=1.0

print(int(c))
print(float(y))
print(float(x))'''

#importing random number

'''import random
print(random.randrange(1,50))
'''
#learn about strringgss


#we use 3 double quotes for a long string

#to print a letter from a string we use

'''a="hello"
print(a[1])'''


#looping through a string

'''for a in "kuldeep":
    print(a)'''

#to print the string length we use the len() function

'''a="kuldeep0"
print(len(a))'''

#to check whether a certain phrase or character  is present in the string or not

'''txt="kuldeep is almost being the best "

print("" in txt)
   '''

#same using if else statement
'''statement="today was a very good day"
if "today" in statement:
    print("yes,'today'is in the statement")

else:
    print("no")

'''

#today we will learn about indexing

'''b="helloworld"
print(b[5:10])'''

#negative indexing
'''a="hello world"
print(a[:-6])'''

#modifying stringss

"""a="hello world"
print(a.upper())
b="HELLO KULDEEP"
print(b.lower())

#removing whitespace

whitespace="   hello world"
print(whitespace.strip()"""


#F-strings
'''age=42
txt=f"my name is kuldeep and my age is {age}"
print(txt)'''

'''price=59
txt=f"the price on mrp is {price}"
print(txt)'''

"""txtt=f"the price is {29*32}"
print(txtt)"""

#boolean methods
'''a=1
b=3
if a>b:
    print("a is greater than b")

else:
    print("false")

print(bool("hello"))
print(bool(23))    

x="hello"
b=33

print(bool(x))
print(bool(b))'''


#python lists
#lists are created using sqr brackets
#lists allows duplicate values

'''this_list=["apple","banana","apple"]
print(this_list)
print(len(this_list))

lis1=["apple",23,True,"banana"]
print(lis1)
print(len(lis1))
print(type(lis1))
'''
#another wAY IF YOU DONT WANT TO USE THE BRACET TO USE THE LIST IS THAT YOU CAN TYPEE LIST


'''abc=list(("apple","ball"))
print(type(abc))
print(len(abc))
print(abc)'''


#there are four collection data types in python
#list=ordered and changeabale
#tuple=ordered and unchangeable
#set=unordered and unchangeable
#dictionary=unordered and changeable


#how to access list itemss


'''abc=list(("apple","banana",23))

statement="hi i am kuldeep and today i want to eat a "

print(statement,abc[:2])
'''

#to print a right angle triangle
'''for i in range(1,10):
    print("*"*i)
'''
'''print("kuldeep")
print("he is a ")'''

#list items

'''thislist=["apple","banana","cherry","applepie","matcha","coldrink"]
thislist[1]="blackcurrent"

#to change a range of lists
thislist[3:5]="matcha","applepie","mango","ramen"'''


#to change two values with one value

'''thislist[3:5]=["mosambi"] 
print(thislist)

#using the insert method

thislist.insert(2,"watermelon")
print(thislist)
#removing an element from the list 
thislist.remove("mosambi")
print(thislist)
'''

#loop list
#this prints all elements in the list one by one
'''thislist=["apple","banana","grape","dragonfruit"]
for x in thislist:
    print(x)'''
#now we will learn how to loop in the list 
#below is a example
'''for i in range(len(thislist)):
    print(thislist[i])'''

#let's learn how to use a while loop 

thislist=["apple","banana","grape"]
i=0
while i<len(thislist):
    print(thislist[i])
    i=i+1   
