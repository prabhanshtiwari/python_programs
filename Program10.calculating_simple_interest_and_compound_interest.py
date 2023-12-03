# Write a program to accept principal amount, rate of interest and time duration from the user calculate simple interest and compound interest.

principal_amount = float(input("Enter principal amount: "))
rate_of_interest = float(input("Enter rate of interest: "))
time = float(input("Enter time: "))

simple_interest = (principal_amount * rate_of_interest * time) / 100
total_amount = principal_amount * (1 + (rate_of_interest / 100) ) ** time
compound_interest = total_amount - principal_amount

print("Simple Interest = ", simple_interest)
print("Compound Interest = ", compound_interest)
