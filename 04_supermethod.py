class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b=2



class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")

    c=3


# k=Employee()
# print(k.a)

# k=Programmer()
# print(k.a,k.b)

k=Manager()
print(k.a,k.b,k.c)
