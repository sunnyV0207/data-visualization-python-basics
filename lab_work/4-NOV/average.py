#Write a program to calculate average of five numbers

# Program to calculate the average of five numbers

# Taking 5 numbers as input from the user
# float() is used so the user can enter decimal numbers as well
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
num5 = float(input("Enter fifth number: "))

# Calculating the sum of all 5 numbers
total = num1 + num2 + num3 + num4 + num5

# Calculating the average
average = total / 5

# Displaying the result
print(f"\nThe average of the five numbers is: {average}")
