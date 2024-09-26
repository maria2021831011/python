from audioop import reverse

list={1,2,3,4}
print(list)
#tupple not change
tupple=(1,2,3,4)

print(tupple)

l = [1, 2, 3, 4, 5]

cl = l.copy()
cl.reverse()

if l == cl:
    print("palindrome")
else:
    print("not palindrome")

