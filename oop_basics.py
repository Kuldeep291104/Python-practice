'''class cricket:
    over=20
    captain="kuldeep"
    v_captain="abhay"

matchday=cricket()
print(matchday.captain,matchday.over)
'''
#instance attribute takes preference over class attribute

# eg

'''test_cricket=cricket()
test_cricket.over=100

print(test_cricket.over,test_cricket.captain)'''

# above is an example of instance attribute



# using self 

'''class Employee:
    language="Python"
    Experience=12

    def getInfo(self):
        print(f"The language is{self.language} and experience is{self.Experience}")



kuldeep=Employee()
kuldeep.language="Python and Html"
kuldeep.getInfo()      '''

#using static method

'''class Employee:
    language="Python"
    Experience=12

    def getInfo(self):
        print(f"The language is{self.language} and experience is{self.Experience}")

    @staticmethod
    def greet():
        print("Good morning")

kuldeep=Employee()
kuldeep.language="Python and Html"
kuldeep.greet()
kuldeep.getInfo()
'''

#init constructor

'''class Employee:
    language="Python"
    Experience=12

    def getInfo(self):
        print(f"The language is{self.language} and experience is{self.Experience}")

    def __init__(self):             #dunder method in python (__init__) automatically calls itself
        print("start")        
        

kuldeep=Employee()
kuldeep.language="Python and Html"
kuldeep.getInfo()      
'''

