#Write a program to calculate simple interest in python.

# Simple Interest Calculator in Python

# Function to calculate simple interest
def calculate_simple_interest(principal, rate, time):
    """
    This function calculates simple interest using the formula:
    Simple Interest = (Principal * Rate * Time) / 100
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest


# Taking user input
# float() is used to allow decimal values if needed
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calling the function and storing the result
interest = calculate_simple_interest(principal, rate, time)

# Displaying the result
print(f"\nThe Simple Interest is: {interest}")
