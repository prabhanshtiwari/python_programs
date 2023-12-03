# Write the python program for Calculating the semi-perimeter(s) and area of the triangle. a ,b & c are three side of triangle whose values are 5,3 & 2 respectively.
# s=(a+b+c)/2
# area=√ (s(s-a)*(s-b)*(s-c)) or use (s(s-a)*(s-b)*(s-c))**0.5

a = 5  # First side of triangle
b = 3  # Second side of triangle
c = 2  # Third side of triangle
s = (a + b + c)/2   # semi-perimeter
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 # area of triangle by heron formula

# Displaying output
print("Semi-perimeter =", s)
print("Area =", area)
