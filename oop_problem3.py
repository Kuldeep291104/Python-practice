# Create a class with a class attribute a;create an object from it and set'a' directly using object.a=o.Does this change the class attribute?


class trial:
    a=4 

o=trial() 
o.a=1
print(o.a)


# yes it changes the attribut