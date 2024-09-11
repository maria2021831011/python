weight=int (input("weight "))
unit=input("k(kl) and pounds :")
if unit=="k":
    converted=weight*0.45
    print("for kg: "+str(converted))
else :
    converted=weight/0.45
    print("for pd: "+str(converted))
