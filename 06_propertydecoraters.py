class employee:
    a=1
    @classmethod
    def show(cls):

        print(f"The value of a is {cls.a}")

    @property
    def name(self):
        return(f"{self.fname} {self.lname}")
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

b=employee()
b.a=45


b.name="kuldeep Rathod"
print(b.lname)