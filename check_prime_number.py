# Program to check if the entered number is prime number or not
number = int(input("Enter a number to check if it is prime or not: "))
list = []
for i in range(1, number+1):
  if number % i == 0:
    list.append(i)
print("List of factors =", list)
number_of_factors = len(list)

if number_of_factors == 2:
  print(number, "is a prime number")
else:
  print(number, "is not a prime number")
