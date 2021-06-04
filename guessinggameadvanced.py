#this is a guessing  advanced version program
#execute the code

import random
import math

random_num=(math.floor(random.random()*10))
random_num1=(math.floor(  random.random()*5))

random_num2=(math.floor(random.random()*5)+1)


def num():
     for ot05 in range(1,3):
        print(f"you  have only {3-ot05}  life  left") 
        lis={random_num+1-random_num1,random_num,random_num+random_num2}
        for  x  in lis:
            print(x)
        inp=int(input("choose  a  any one number  from above line:"))
        if ot05==2:
            print("you lose try again")
        elif inp !=random_num:
            print("wrong")
        elif inp==random_num:
            print(f"  Well done! you did in {3-ot05}  life ")   
            break
        
        else:
            print("make  sure you  type  valid")
        
        
  



num()              



