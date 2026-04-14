#dict is mutable
#dict stores in key value pairs

marks={"kuldeep":100,
       "naman":98,
       "rashi":78,
       "abhay":67 

}
#dict methods

#to print dict items
print(marks.items())


#to print the key 
print(marks.keys())

#to print the values
print(marks.values())
#to update 
marks.update({"kuldeep":99,"Roshni":97})

print(marks)


#to get a specified this will never give an error
print(marks.get("kuldeep"))