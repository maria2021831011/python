
def work():
    word = "sak"
    li_no = 1
    with open("hi.txt", "r") as f:
        for line in f:
            if word in line:
                print(li_no)
                return
            li_no += 1
    return -1

work()
