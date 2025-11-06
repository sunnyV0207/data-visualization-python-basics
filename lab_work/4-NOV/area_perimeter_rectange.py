#Write a program to calculate area and perimeter of the rectangle in python

# Program to calculate the Area and Perimeter of a Rectangle

# Function to calculate area of rectangle
def calculate_area(length, width):
    """
    Formula:
    Area = Length × Width
    """
    return length * width


# Function to calculate perimeter of rectangle
def calculate_perimeter(length, width):
    """
    Formula:
    Perimeter = 2 × (Length + Width)
    """
    return 2 * (length + width)


# Taking input from the user
# float() allows decimal values like 5.5, 10.25 etc.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating area and perimeter
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

# Displaying the results
print(f"\nArea of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
