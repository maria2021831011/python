
class s:
    def __init__(self,bb,cc):
        self.bb=bb
        self.cc=cc

    def debit(self,am):
        self.bb-=am
        print("devit for",am)
        print(self.get())

    def credit(self, am):
        self.bb += am
        print("devit for", am)
        print(self.get())

    def get(self):
        return self.bb

s1=s(1000,1200)
s1.debit(200)
s1.credit(300)
