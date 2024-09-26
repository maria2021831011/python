collection={1,2,3,4,4,4,4,}
print(collection)
c=set()#empty set
c.add(1)
c.add(2)
c.add(3)
c.add("ho")
c.add((1,2,3))

print(c)
print(len(c))
c.clear()
print(len(c))
print(collection.pop())
set1={1,2,3}
collection1={4,6,3,7}
print(set1.union(collection1))
print(set1.intersection(collection1))
dictonaryyy={
    "sub":"ict",
    "topic":["hi","hlw"]
}
print(dictonaryyy)
s={
    "c++","puthon","c","c++","c","java"
}
print(len(s))
marks={}
x=input("enter your marks phy: ")
marks[x]=x
x=input("enter your marks chem: ")
marks[x]=x
x=input("enter your marks bio: ")
marks[x]=x
x=input("enter your marks math: ")
marks[x]=x
print(marks)
j={9,'9.0'}
print(j)
values={
    ("int ",9),
    ("float",9.0)
}
print(values)

