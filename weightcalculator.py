#here you  find your weight in kg or pound
def weight_converter(kg=0,pound=0):
    weight=int(input("WHAT IS  YOUR  WEIGHT  "))
    prm=input(" IS YOUR WEIGHT IS IN POUND (P) OR KILOG GRAM (K)")
    if prm.upper()=="P":
        print(weight//2.205,"KG")
    elif prm.upper()=="K" :
        print(weight* 2.205,"p") 
    else:
        print("MAKE  SURE  YOU  TYPE  CORRECT ")      
    




weight_converter()    
    






