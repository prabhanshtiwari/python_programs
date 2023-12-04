 # Write a program to swap two accepted values with addition and subtraction method.
 
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
 
print("Before swappping: ")
print("Value of a =", a)
print("Value of b =", b)

a = a + b
b = a - b
a = a - b

print("After swappping: ")
print("Value of a =", a)
print("Value of b =", b)
