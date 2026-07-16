#Task 2
#Exercise 1
print("Task 2")
def multiply_numbers(a, b):
    return a * b
result = multiply_numbers(12, 7)
print("Product:", result)
#Exercise 2
def calculate_area(width, height):
    return width * height
user_width = float(input("Enter the width: "))
user_height = float(input("Enter the height: "))
area = calculate_area(user_width, user_height)
print("The area is:", area)
#Exercise 3
def calculate_box_volume(length, width, height):
    return length * width * height
l = float(input("Enter the length: "))
w = float(input("Enter the width: "))
h = float(input("Enter the height: "))
volume = calculate_box_volume(l, w, h)
print("The volume of the box is:", volume)