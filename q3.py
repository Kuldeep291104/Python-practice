# create a class 'employee' and add salary and increment properties to it.
# write a method 'salary after increment' with @property decorater with a setter which changes the value of increment based on salary
class Employee:
    salary = 234
    increment = 20
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment=((salary/self.salary)-1)*100


k=Employee()
# print(k.salaryafterincrement)
k.salaryafterincrement=280
print(k.increment)