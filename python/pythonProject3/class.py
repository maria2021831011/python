"""class car:
    name="marcedes"
    brand="Ford"

c1=car()
print(c1.name)
print(c1.brand)"""
class student:
    def __init__(self):
        pass

    def __init__(self,name,brand,course): #constructor
        self.name=name
        self.brand=brand
        self.course=course

s1=student("marcedes","Ford","Ford")
print(s1.name)
print(s1.brand)
print(s1.course)