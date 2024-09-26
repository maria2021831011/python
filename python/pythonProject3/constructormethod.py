class st:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gets(self):
        print( self.x)

    @staticmethod
    def stat():
        print(" i am static not use self")

    def get(self):
        sum=0
        for val in self.y:
            sum+=val
        print( sum)

s1=st("maria",[16,20,50,70])
s1.get()
s1.gets()
s1.stat()