#Write a program to find out speed when distance and time has been given.

# Program to calculate Speed when Distance and Time are given

# Formula:
# Speed = Distance / Time

# Taking user input
# float() is used to allow decimal values (e.g., 12.5 km, 1.2 hours)
distance = float(input("Enter the distance travelled (in km): "))
time = float(input("Enter the time taken (in hours): "))

# Checking to avoid division by zero
if time == 0:
    print("\nTime cannot be zero. Speed cannot be calculated.")
else:
    # Calculating speed
    speed = distance / time
    
    # Displaying the result
    print(f"\nThe speed is: {speed} km/h")
