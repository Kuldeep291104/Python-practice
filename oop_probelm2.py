# write a class "calculator" capable of finding square,cube and sqrt of a number.

import math
class calculator():
    def __init__(self,n):
        self.n=n


    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {math.sqrt(self.n)}")

b=int(input("enter a number"))
a=calculator(b)
a.square()
a.cube()
a.squareroot()