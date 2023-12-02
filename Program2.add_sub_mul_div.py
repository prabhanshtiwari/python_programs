# Write a python Program for addition, subtraction, multiplication & division.

# Addition
print("Addition:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
addition = num1 + num2
print("Addition =",num1 ,"+", num2, "=", addition)

# Subtraction
print("Subtraction:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
subtraction = num1 - num2
print("Subtraction =",num1 ,"-", num2, "=", subtraction)

# Multiplication
print("Multiplication:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
product = num1 * num2
print("Product =",num1 ,"*", num2, "=", product)

# Division
print("Division:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num2 != 0:
    quotient = num1 / num2
else:
    print("Can't divide by zero")
print("Quotient =",num1 ,"/", num2, "=", quotient)
