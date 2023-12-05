# Write a python Program to accept value from user to Check Whether a Number is Prime or not. 

number = int(input("Enter a number: "))
list = []
for i in range(1, number + 1):
    if number % i == 0:
        list.append(i)
if len(list) == 2:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
