# Write a python program to find the largest and smallest among three entered numbers. 

num1 = int(input("Enter first number(num1): "))
num2 = int(input("Enter second number(num2): "))
num3 = int(input("Enter third number(num3): "))
# list = [num1, num2, num3]
# list.sort()
# print("Largest number: ", list[-1])
# print("Smallest number: ", list[0])

# check largest number
if num1 > num2 and num1 > num2:
    print(num1, "is largest number.")
elif num2 > num1 and num2 > num3:
    print(num2, "is largest number.")
else:
    print(num3, "is largest number.")

# check smallest number
if num1 < num2 and num1 < num2:
    print(num1, "is smallest number.")
elif num2 < num1 and num2 < num3:
    print(num2, "is smallest number.")
else:
    print(num3, "is smallest number.")
