c=0
with open("gi.txt","r") as f:
    data=f.read()
    print(data)
    num=data.split(",")
    for i  in num:
        if(int(i)%2==0):
            c+=1

print(c)