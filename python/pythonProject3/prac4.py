MARKS = int(input("Enter the number of marks: "))
if MARKS >= 80:
    GRADE = "A"
elif 70 <= MARKS < 80:
    GRADE = "B"
else:
    GRADE = "C"  # Option for grades below 70
print("The grade is: ",GRADE)
age=int(input("Enter your age: "))
if age>18:
    if age>80:
        print("not")
    else:
        print("yes")
else:
    print("You are a teenager")

