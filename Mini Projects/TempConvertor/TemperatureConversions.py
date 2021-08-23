def celsius(to, num):
    if to == 2:
        return f"{num}°C = {round((num * 1.8) + 32, 2)}°F"
    else:
        return f"{num}°C = {round(num + 273.15, 2)}K"


def fahrenheit(to, num):
    if to == 1:
        return f"{num}°F = {round((num - 32) / 1.8, 2)}°C"
    else:
        return f"{num}°F = {round(((num - 32) / 1.8) + 273.15, 2)}K"


def kelvin(to, num):
    if to == 1:
        return f"{num}K = {round(num - 273.15, 2)}°C"
    else:
        return f"{num}K = {round(((num - 273.15) * 1.8) + 32, 2)}°F"


print("Welcome to the Temperature Convertor. Please select your conversions below:\n1. Celsius\n2. Fahrenheit\n3. "
      "Kelvin")
first = input("From:")
second = input("To:")
number = input("Value:")

if not all(x.isnumeric() for x in [first, second, number]):
    print("Not all inputs are numbers. Please try again.")
elif not 0 < int(first) < 4 and 0 < int(second) < 4:
    print("Your conversion inputs were not in range of the options.")
elif first == second:
    print("Your input is the same as your output.")
else:
    first, second, number = int(first), int(second), int(number)
    if first == 1:
        print(celsius(second, number))
    elif first == 2:
        print(fahrenheit(second, number))
    else:
        print(kelvin(second, number))
