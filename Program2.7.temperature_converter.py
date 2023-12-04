# Write a program to accept the value in Fahrenheit and convert it into Celsius, kelvin

fahrenheit_value = float(input("Enter temperature in fahrenheit: "))

celsius_value = (fahrenheit_value - 32) / 1.8
kelvin_value =  (fahrenheit_value + 459.67) / 1.8

print("Temperature in Celsius = ", celsius_value)
print("Temperature in Kelvin = ", kelvin_value)
