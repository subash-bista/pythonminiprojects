#this is  not  a  actual  car game nor  a cui game
#it  just like a  car engine execute the code 
print("CAR  GAME  IS  READY IF YOU DID'NT  FIND THE OPTION TRY using in terminal  'HELP'")
run=" "
while True:
    run=input(">")
    if run.upper()=="HELP":
        help_car=("start-to start game\nstop-to stop game\nquit- exit the game")
        print(help_car)
    
    elif run.upper()=="START":
       print('CAR IS STARTED ........')  
    
    elif run.upper()=="STOP":
        print("CAR IS  STOPPED")  
    elif run.upper()=="QUIT":
        break    
  
    else:
        print("Please  use the given command","start-to start game\nstop-to stop game\nquit game") 

             


