# Write a program to print the sum of digits of a number using for loop. 
number = int(input("Enter a number: "))
temp = number
sum_of_digits = 0
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10
print("Sum of digits of", number, "=", sum_of_digits)
