with open("demo4.txt","r") as f:
    dem=f.read()
    print(dem)
    with open("demo4.txt", "w") as f:
        f.write("ji")

