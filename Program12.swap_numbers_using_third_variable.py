#Write a program to swap two accepted values from user using third or temporary variable.

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))

print("Before Swapping:")
print("Value of a: ", a)
print("Value of b: ", b)

c = a
a = b
b = c

print("After Swapping:")
print("Value of a: ", a)
print("Value of b: ", b)
