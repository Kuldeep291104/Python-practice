# write a class Train which has methods to book a ticket,get status(no of seats)and get fare information of train running under indian railways
from random import randint
class Train:

    def __init__(self,train_no):
        self.train_no=train_no

    def book(self,fro,to):

        print(f"Your ticket is successfully booked in train number {self.train_no},from{fro} to {to}")

    def fare(self):

        print(f"Your amt is{randint(222,999)}")

karnavati=Train(12933)

karnavati.book("Ahmedabad","Borivali")

karnavati.fare()