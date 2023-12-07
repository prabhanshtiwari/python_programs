# Write a python program to check number is Armstrong or not.
num = int(input("Enter a number: "))
length = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** length)
    temp = temp // 10

if sum == num:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")
