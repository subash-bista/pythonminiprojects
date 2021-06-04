#this  is  a faulty calculator which mean it excute wrong calculation
#of expression 45*3=555 ,56+9=77, 56/6=4 these  all are wrong cal
#except this all work fine
num1=int(input("type  a  number:"))
num2=int(input("type another number:"))
symbol=input("""CHOOSE add for "+" subtract  for "-" choose multiply for "*" choose divide for "/" """)
if num1==45 and num2==3 and symbol=="*":
    print(555)#number 45*3
elif num1==56 and num2==9 and symbol=="+":
    print(77) #number 56+9
elif num1==56 and num2==6 and symbol=="/":
    print(4)  #number 56/6   
elif symbol=="*":
    print(num1*num2)    
elif symbol=="/":
    print(num1/num2)

elif symbol=="-":
    print(num1-num2)
elif symbol=="+":
    print(num1+num2) 
else:
    print("please  add a  valid number 'error'")    



