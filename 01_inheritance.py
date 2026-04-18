class Employee():
    company="ITC"
    name="Kuldeep"
    def show(self):
        print(f"The name of the Employee is {self.name}")
class Programmer(Employee):
    company="ITC INFOTECH"
    def showlanguage(self):
        print(f"The name is{self.name}")

a=Employee()
b=Programmer()
b.showlanguage()

