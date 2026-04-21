#the game() function in a program lets a user play a game and returns the score as an integer.You need
#to read a file "hi-score.txt" which is earlier blank or contains the previous high score.You need to write 
# a program to update the hi-score whenever the game() function breaks the high score.
import random as rd

def game():
    print("you are playing the game")
    score=rd.randint(1,100)
    #fetch high score
    with open("hiscore.txt")as f:       
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score:{score}")
    if(score>hiscore):
         with open("hiscore.txt","w")as f:
            f.write((str(score)))
    return score
game() 
    