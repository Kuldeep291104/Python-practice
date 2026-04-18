class Employee():
    company="ITC"
    name="Kuldeep"
    def show(self):
        print(f"The name of the Employee is {self.name}")


class coder():
    language="Python"
        
    def show():
        def printlanguage(self):
            print(f"Your language is {self.language}")






class Programmer(Employee,coder):
    company="ITC INFOTECH"
    def showlanguage(self):
        print(f"The name is {self.company} and the language is{self.language}")

a=Employee()
b=Programmer()

b.show()
b.showlanguage()


