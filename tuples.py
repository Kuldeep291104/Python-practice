#This is a tuple class
#we can create an empty tuple but what if we had to make a tuple with 1 integer
#a=(1,)
#above will indicate the tuple class
#tuples are immutable
#lists are mutable



#tuple methods
'''a=(1,"kuldeep",25.3,1)
print(a)
no=a.count(1)
print(no)'''
#count helps to count how many times a tuple element is repeated


#here index helps us to know the position of a specific element
#print(a.index(1))


#concatenation of 2 tuples

'''a=(1,"kuldeep")
b=(2,"abhay")

concatenated=a+b
print(concatenated)
'''
#repetiton of tuples

'''print(concatenated*3)
'''
#membership of tuples
'''print(2 in a)
'''

#length
'''print(len(concatenated))
'''

#built in function highest lowest 

'''print(min(a))
print(max(a))
print(sum(a))'''

#packing functions

'''t=(1,2,3)

k,m,f=t
print(m)
'''
#tuple practice
'''marks=[]
f1=(input("enter your marks name: "))
marks.append(f1)
f2=(input("enter your marks name:"))
marks.append(f2)
f3=(input("enter your marks name:"))
marks.append(f3)
f4=(input("enter your marks name:"))
marks.append(f4)
f5=(input("enter your marks name:"))
marks.append(f5)
print(marks)
'''

#problem2
''''marks=[]
f1=(int(input("enter your marks name: ")))
marks.append(f1)
f2=(int(input("enter your marks name:")))
marks.append(f2)
f3=(int(input("enter your marks name:")))
marks.append(f3)
f4=(int(input("enter your marks name:")))
marks.append(f4)
f5=(int(input("enter your marks name:")))
marks.append(f5)
marks.sort()
print(marks)'''


#[roblem 4 ]
'''a=[1,35,6,2,3]
print(sum(a))'''

#problem 5

a=(7,0,8,0,0,9)
c=a.count(0)
print(c)