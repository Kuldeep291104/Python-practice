#to create empty set
'''a=set()
print(type(a))
b={}
print(type(b))
c={1,2,3,}
print(type(c))'''
#Why to use sets??
#because sets dont have repetitive elements\

#methods for set

#Add an element in the set
s={1,42,51,11,24,"kuldeep"}  #note this tag adds only one element
s.add(32)
print(s)

#update an element on set
s.update([45,66])  #this tag allows a user to add one or more element in the set

#Remove an element from the set
s.remove("kuldeep")  #using this tag will give an error if the element we wANT TO REMOVE IS NOT FOUND
print(s)

#DISCARD AN ELEMENT (USING THIS THE TERMINAL WILL NOT SHOW AN ERROR EVEN IF THE ELEMENT IUS NOT PRESENT ON THE SET)
s.discard("nib")
print(s)


#to choose a random element from the set
c=s.pop()

#clear() removes all elements from the set
s.clear()
print(s)
print(c)


#manipulation using 2 sets

s1={14,28,72,65,55}
s2={72,21,44,56,23}

print(s1.union(s2))
print(s1.intersection(s2))

