"""use delete function"""
"""class nothing:
    def __init__(self,a,b):
        self.a=a
        self.b=b

s1=nothing(10,20)

del s1.a
print(s1.a)"""
#private acces
class pri:
    __name="maria"
    def __hellow(self):
        print("HI MARIA")
    def welcome(self):
        self.__hellow()

s=pri()
print(s.welcome())