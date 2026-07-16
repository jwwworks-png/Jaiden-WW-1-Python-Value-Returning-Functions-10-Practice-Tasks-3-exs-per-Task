#1
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
principal = 4000
rate = 5
time = 4
interest = simple_interest(principal, rate, time)
print("Interest:", interest)
#2
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100
user_principal = float(input("Enter the Principal: "))
user_rate = float(input("Enter the Rate (%): "))
user_time = float(input("Enter the Time (years): "))
interest = simple_interest(user_principal, user_rate, user_time)
print("Interest:", interest)
#3
def calculate_all(principal, rate, time):
    interest = (principal * rate * time) / 100
    final_amount = principal + interest
    return interest, final_amount
principal = 4000
rate = 5
time = 4
interest, final_amount = calculate_all(principal, rate, time)
print("Interest:", interest)
print("Final Amount:", final_amount)