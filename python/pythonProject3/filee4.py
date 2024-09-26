word="am"
with open("pu.txt","r") as f:
    dop=f.read()
    new=dop.replace("python","java")
    print(new)
    if(new.find(word)!=-1):
        print("yes")
    else:
       print("no  ")