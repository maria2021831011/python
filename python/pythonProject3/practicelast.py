"""import math


class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius

c=circle(3)
print(c.area())
print(c.perimeter())"""
"""class inh:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height


class sub(inh):
    def __init__(self,course,yr,dept):
        self.course = course
        self.yr = yr
        self.dept = dept

    def show(self):
        super().__init__("maria",21,5.2)
        print("NAME :"+str(self.name))
        print("AGE :"+str(self.age))
        print("HEIGHT:"+str(self.height))
        print("COURSE :"+str(self.course))
        print("DEPT :"+str(self.dept))
        print("YEAR :"+str(self.yr))



c=sub("sss" ,2021,"swe")
print(c.show())"""
class A:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # Custom greater-than comparison for 'price'
    def __gt__(self, other):
        return self.price > other.price


# Create two instances of class A
or1 = A(1, 120)
or2 = A(2, 220)

# Using the custom comparison method (__gt__)
print(or1 > or2)  # Output: False, because 120 < 220

# You can also directly compare items if needed
print(or1.item > or2.item)  # Output: False
