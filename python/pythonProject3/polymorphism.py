class Poly:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def complex(self):
        # Print the complex number in the form x + yi
        print(f"{self.x}i + {self.y}j")

    def __add__(self, num2):
        # Add the x and y values of two Poly objects
        n1 = self.x + num2.x
        n2 = self.y + num2.y
        # Return a new Poly object with the resulting x and y
        return Poly(n1, n2)


# Create two instances of the Poly class
num1 = Poly(7, 9)
num1.complex()  # Output: 7i + 9j

num2 = Poly(3, 5)
num2.complex()  # Output: 3i + 5j

# Add the two instances
num3 = num1 + num2  # Uses the __add__ method

# Print the result of the addition
num3.complex()  # Output: 10i + 14j
