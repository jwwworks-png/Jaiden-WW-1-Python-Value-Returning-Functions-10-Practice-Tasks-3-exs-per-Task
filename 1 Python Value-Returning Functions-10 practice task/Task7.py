#1
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
temperature = celsius_to_fahrenheit(30)
print("Temperature:", temperature)
#2
celsius_input = float(input("Enter Celsius temperature: "))
fahrenheit = (celsius_input * 9 / 5) + 32
print(f"{celsius_input}°C")
print(f"{fahrenheit}°F")
#3
def get_weather_category(celsius):
    if celsius <= 0:
        return "Freezing"
    elif celsius <= 15:
        return "Cold"
    elif celsius <= 25:
        return "Warm"
    else:
        return "Hot"
celsius_val = 20
fahrenheit_val = (celsius_val * 9 / 5) + 32
weather_type = get_weather_category(celsius_val)
print(f"{celsius_val}°C")
print(f"{fahrenheit_val}°F")
print("Weather:", weather_type)