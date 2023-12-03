# Write a python program to calculate area and perimeter of a rectangle,
# Area = length * breadth &
# Perimeter = 2 * (length + breadth)

length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))

area = length * breadth  # calculating area of rectangle
perimeter = 2 * (length + breadth)  # calculating perimeter of rectangle

print("Area of Rectangle: ", area)
print("Perimeter of Rectangle: ", perimeter)
