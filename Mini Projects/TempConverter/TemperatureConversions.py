def celsius(to, n):
    return f"{n}°C = {round((n * 1.8) + 32, 2)}°F" if to == 2 else f"{n}°C = {round(n + 273.15, 2)}K"


def fahrenheit(to, n):
    return f"{n}°F = {round((n - 32) / 1.8, 2)}°C" if to == 1 else f"{n}°F = {round(((n - 32) / 1.8) + 273.15, 2)}K"


def kelvin(to, n):
    return f"{n}K = {round(n - 273.15, 2)}°C" if to == 1 else f"{n}K = {round(((n - 273.15) * 1.8) + 32, 2)}°F"


print("Welcome to the Temperature Convertor. Please select your conversions below:\n1. Celsius\n2. Fahrenheit\n3. "
      "Kelvin")
in_, out, number = input("From:"), input("To:"), input("Value:")

if all(x.isnumeric() for x in [in_, out, number]) and int(in_) and int(out) in range(0, 4) and in_ != out:
    in_, out, number = int(in_), int(out), int(number)
    if in_ == 1:
        print(celsius(out, number))
    elif in_ == 2:
        print(fahrenheit(out, number))
    else:
        print(kelvin(out, number))
else:
    print("An error has occurred.")
