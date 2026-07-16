#1
def weekly_pay(hours, rate):
    return hours * rate
pay = weekly_pay(40, 22)
print("Weekly Pay: $", pay)
#2
def weekly_pay(hours, rate):
    return hours * rate
name = input("Enter Employee Name: ")
hours = float(input("Enter Hours Worked: "))
rate = float(input("Enter Hourly Rate: "))
pay = weekly_pay(hours, rate)
print(f"\nEmployee: {name}")
print(f"Weekly Pay = ${pay}")
#3
def weekly_pay(hours, rate):
    return hours * rate

# Employee 1
name1 = input("Enter Employee 1 Name: ")
hours1 = float(input("Enter Hours Worked: "))
rate1 = float(input("Enter Hourly Rate: "))
pay1 = weekly_pay(hours1, rate1)

# Employee 2
name2 = input("Enter Employee 2 Name: ")
hours2 = float(input("Enter Hours Worked: "))
rate2 = float(input("Enter Hourly Rate: "))
pay2 = weekly_pay(hours2, rate2)

# Employee 3
name3 = input("Enter Employee 3 Name: ")
hours3 = float(input("Enter Hours Worked: "))
rate3 = float(input("Enter Hourly Rate: "))
pay3 = weekly_pay(hours3, rate3)
grand_payroll = pay1 + pay2 + pay3
print(f"\n{name1}: ${pay1}")
print(f"{name2}: ${pay2}")
print(f"{name3}: ${pay3}")
print(f"Grand Payroll = ${grand_payroll}")