'''class employee:
    a=1
    def show(self):

        print(f"The value of a is {self.a}")


b=employee()
b.a=45
b.show()
'''
# Above shows the instance attribute so to obtain the class attribue we use class method
class employee:
    a=1
    @classmethod
    def show(cls):

        print(f"The value of a is {cls.a}")


b=employee()
b.a=45
b.show()
