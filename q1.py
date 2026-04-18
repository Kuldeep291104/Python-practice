# create a class(2-d vector) and use it to create anothrr class representing a 3-d vector

class vector:

    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The vector is {self.i} + {self.j}")

class treedvector(vector):

    def __init__(self, i, j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"The vectors are {self.i } + {self.j } + {self.k}")

        

a=treedvector(1,2,4)
b=vector(1,2)

a.show()


       
        