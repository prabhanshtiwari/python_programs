# Write a program to accept value in rupee and convert it into dollar($) and pounds.

INR_value = float(input("Enter value in INR i.e., rupee: "))

USD_value = INR_value * 0.012
GBP_value = INR_value * 0.0095

print(f"{INR_value} INR = {USD_value} USD")
print(f"{INR_value} INR = {GBP_value} pounds")
