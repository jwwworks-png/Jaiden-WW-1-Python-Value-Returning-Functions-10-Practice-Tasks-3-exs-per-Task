#1
def hours_to_minutes(hours):
    return hours * 60
minutes = hours_to_minutes(5)
print("Minutes:", minutes)
#2
hours_input = float(input("Enter hours: "))
minutes = hours_input * 60
print("Hours:", hours_input)
print("Minutes:", minutes)
#3
def convert_time(hours):
    minutes = hours * 60
    seconds = minutes * 60  
    return minutes, seconds
hours_val = 2
mins, secs = convert_time(hours_val)
print("Hours =", hours_val)
print("Minutes =", mins)
print("Seconds =", secs)
