# Write a program to read a number n and compute n+nn+nnn.

n = input("Enter a number: ")
nn = n + n
nnn = n + n + n

result = int(n) + int(nn) + int(nnn)

print("n + nn + nnn =", result)
