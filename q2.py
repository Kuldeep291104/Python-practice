# create a class python 'pets' from  a class 'animals' and further create a class 'dog' from 'pets'.Add a 'bark' method to class 'dog'  

class Animal():
    pass

class pet(Animal):
    pass

class dog(pet):
    @staticmethod
    def bark():
        print("BOW BOW")


baebo=dog()
baebo.bark()
