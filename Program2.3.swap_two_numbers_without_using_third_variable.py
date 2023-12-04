# Write a program to swap two accepted values from user without using temporary variable 

# Accept two values from the user
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

# Print the values before swapping
print(f"Before swapping: a = {a}, b = {b}")

# Swap the values without using a temporary variable
a, b = b, a

# Print the values after swapping
print(f"After swapping: a = {a}, b = {b}")
