class Company():
    companyname="Amazon"
    def show(self):
       
        print(f"The name of the company is: {self.companyname}")


class manager(Company):
    name="Kuldeep"

    def new(self):
        
        print(f"The comapny in which {self.name} works is {self.companyname}")


class Employee(manager):

    mm="Rahul"

    def nee(self):
        print(f"The comapny in which {self.name}  is manager {self.companyname} and employee name is {self.mm}")


a=Company()
b=manager()
c=Employee()

c.nee()