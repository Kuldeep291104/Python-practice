'''import random as rd

'''
rock=1 
paper=2 
scissor=3
'''


computer=rd.choice([1,2,3])
yourstr=(input("R,p or s"))
youdict = {"r":1,"p":2,"s":3,}
reversedict={1:"rock",2:"paper",3:"scissor"}

yournum=youdict[yourstr]
print(f"You chose{reversedict[yournum]}\nComputer chose{reversedict[computer]}")


if(computer==1 and yournum==1):
    print("Draw")
elif(computer==1 and yournum==2):
    print("you win")
elif(computer==1 and yournum==3):
    print("you loose")


elif(computer==2 and yournum==1):
    print("you win")
elif(computer==2 and yournum==2):
    print("Draw")
elif(computer==2 and yournum==3):
    print("you loose")



elif(computer==3 and yournum==1):
    print("you win")
elif(computer==3 and yournum==2):
    print("you loose")
elif(computer==3 and yournum==3):
    print("Draw")

'''
import random as rd

youdict = {"r":1, "p":2, "s":3}
reversedict = {1:"rock", 2:"paper", 3:"scissor"}

user_score = 0
computer_score = 0

while user_score < 5 and computer_score < 5:
    computer = rd.choice([1, 2, 3])
    
    yourstr = input("\nR, P or S: ").lower()
    
    if yourstr not in youdict:
        print("Invalid input, try again!")
        continue

    yournum = youdict[yourstr]

    print(f"You chose {reversedict[yournum]}")
    print(f"Computer chose {reversedict[computer]}")

    if computer == yournum:
        print("Draw")

    elif (yournum == 1 and computer == 3) or \
         (yournum == 2 and computer == 1) or \
         (yournum == 3 and computer == 2):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

# Final winner
if user_score == 5:
    print("\n🎉 You won the game!")
else:
    print("\n💻 Computer won the game!")