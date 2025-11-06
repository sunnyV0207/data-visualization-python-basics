# Program to check whether three sides form a triangle and identify its type

class TriangleChecker:
    def __init__(self, side1, side2, side3):
        self.a = side1
        self.b = side2
        self.c = side3

    # Function to check if sides form a valid triangle
    def is_valid_triangle(self):
        return (self.a + self.b > self.c) and \
               (self.b + self.c > self.a) and \
               (self.c + self.a > self.b)

    # Function to find the type of triangle
    def triangle_type(self):
        if self.a == self.b == self.c:
            return "Equilateral Triangle"
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"


# -------- Main Program --------
# Taking input from user
side1 = float(input("Enter length of first side: "))
side2 = float(input("Enter length of second side: "))
side3 = float(input("Enter length of third side: "))

# Creating object
triangle = TriangleChecker(side1, side2, side3)

# Checking validity and type
if triangle.is_valid_triangle():
    print("The given sides form a triangle.")
    print("Type of Triangle:", triangle.triangle_type())
else:
    print("The given sides do NOT form a triangle.")
