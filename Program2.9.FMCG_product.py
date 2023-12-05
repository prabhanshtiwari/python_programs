# Write a program to accept any FMCG product details like product name, product price, quantity, calculate the total price.

product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity of the product: "))
total_price = product_price * quantity

print("Total Price =", total_price)
