# Write a program to check whether a number is Palindrome or not.

number = int(input("Enter a number: "))
if str(number) == str(number)[::-1]:
    print(number, "is a Palindrome Number")
else:
    print(number, "is not a Palindrome Number")
