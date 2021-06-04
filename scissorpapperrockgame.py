import random
import math
print("Welcome  to rock papper scissior game")
inp=input("rock for 'r' papper for 'p' scissior for 's':").lower()
def computer():
    com_ran= math.floor(random.random()*3+1) 
    if com_ran==1:
        com_ran="r"  
    elif com_ran==2:
        com_ran="p"
    elif com_ran==3:
        com_ran="s"
     #computer condition
    if com_ran=="r":
        print("computer choose rock 'r'") 
    elif com_ran=="p":
        print("computer choose papper 'p'") 
    elif com_ran=="s":
        print("computer choose scissor 's'")       
    #person  condition 
    if inp=="r":
        print("you choose rock 'r'") 
    elif inp=="p":
        print("you choose papper 'p'") 
    elif inp=="s":
        print("you choose scissor 's'")       
 #  it  is a function nested(all processing done here)  
    def process():
        if com_ran==inp:
            print("tie")
        if com_ran=="r":
            if inp=="p":
                print("you win")
            elif inp=="s":
                print("you lose")     
        if com_ran=="p":
            if inp=="s":
                print("you win")
            elif inp=="r":
                print("you lose")     
        if com_ran=="s":
            if inp=="r":
                print("you win")
            elif inp=="p":
                print("you lose")   
    process()              
computer()



