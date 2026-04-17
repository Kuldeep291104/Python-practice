# can you change the self-parameter inside a class to something else(say "slf"),Try changing self to "slf" see the effects


# lets take previos question self into this to check


class Programmer:
    def __init__(slf,name,age,salary):
        slf.name= name
        slf.age=age
        slf.salary=salary

kuldeep=Programmer("kuldeep",21,50000)
print(kuldeep.age,kuldeep.name)

Rohan=Programmer("Rohan",21,40000)
print("Age of Rohan is ",Rohan.age)\



# Therefore it dows not make any change