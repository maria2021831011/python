class sup:
    def __init__(self ,type):
        self.type = type

    def start(self):
        print("chollo")



class sub(sup):
    def __init__(self ,type,name):
        super().__init__(type)
        self.name = name
        super().start()




c=sub("yellow","car")
print(c.name)