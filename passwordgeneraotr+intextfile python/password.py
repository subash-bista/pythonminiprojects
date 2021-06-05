import  random
import math
alpha=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
symbol=("@","#","$","%","^","&","**")
symbol2=("@","#","$","%","^","&","**")
ranom_alpha=math.floor(random.random()*26)
ranom_num2=math.floor(random.random()*12)
ranom_num3=math.floor(random.random()*20)
ranom_num4=math.floor(random.random()*26)
ranom_num5=math.floor(random.random()*16)
ranom_symbol=math.floor(random.random()*6)
ranom_symbol_2=math.floor(random.random()*6)
random_pass_num_15=math.floor(random.random()*15)
random_pass_num_70=math.floor(random.random()*70)
pass_alpha=alpha[ranom_alpha]+ str(random_pass_num_15)+str(random_pass_num_70)+ str(symbol2[ranom_symbol_2])+ str(alpha[ranom_num2])+str(ranom_num3)+ str(symbol[ranom_symbol])+str(alpha[ranom_num4])+str(alpha[ranom_num5])



output=(f"your password is {pass_alpha} \n")
with open("password.txt","a") as w:
    w.write(output)