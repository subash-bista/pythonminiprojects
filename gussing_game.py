num=10
numguess=1
print("GUESS  A  NUMBER  BETWEEN 1  AND 20")
while numguess<4:
    inp=int(input(">"))
    if inp<num:
        print("LOW")
    elif inp>num:
        print('HIGH')
    elif  inp==num:
        print(f'YOU DID IT  IN {numguess}  STEP')
        break
    print(f"{4-numguess} STEP LEFT")
    numguess+=1

