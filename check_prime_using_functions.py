def check_prime(number):
  list = []
  for i in range(1, number+1):
    if number % i == 0:
      list.append(i)
  length = len(list)
  if length == 2:
    return "Prime"
  else:
    return "Not Prime"

number = int(input("Enter a number: "))
print(number, "is", check_prime(number), "Number")
