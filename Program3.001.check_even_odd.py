# Write a python program to accept values from user to check whether a given number is even or odd. 

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")
