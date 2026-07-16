#Task 1
#Exercise 1
print("Task 1")
def add_numbers(num1, num2):
    return num1 + num2
answer = add_numbers(18, 42)
print("Answer =", answer)
#Exercise 2
def add_numbers(num1, num2):
    return num1 + num2
user_num1 = int(input("Enter first number: "))
user_num2 = int(input("Enter second number: "))
total=user_num1 + user_num2
print("The total is:", total)
#Exercise 3
def add_three_numbers(num1, num2, num3):
    sum_total = num1 + num2 + num3
    return sum_total
num_input1 = int(input("Enter number 1: "))
num_input2 = int(input("Enter number 2: "))
num_input3 = int(input("Enter number 3: "))
final_total = add_three_numbers(num_input1, num_input2, num_input3)
print("Total =", final_total)
