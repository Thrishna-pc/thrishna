

import importarea 


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rect_area = importarea.area_of_rectangle(length, width)
print(f"Area of Rectangle = {rect_area:.2f}")


radius = float(input("\nEnter the radius of the circle: "))
circle_area = importarea.area_of_circle(radius)
print(f"Area of Circle = {importarea:.2f}")
