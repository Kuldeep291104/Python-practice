#create a class programmer for storing information of few programmers working at microsoft.


class Programmer:
    def __init__(self,name,age,salary):
        self.name= name
        self.age=age
        self.salary=salary

kuldeep=Programmer("kuldeep",21,50000)
print(kuldeep.age,kuldeep.name)

Rohan=Programmer("Rohan",21,40000)
print("Age of Rohan is ",Rohan.age)