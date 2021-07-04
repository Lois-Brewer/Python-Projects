import re


def filter(equation_string):
    # Filters input string to an equation
    equation_string = re.findall("[0-9^*%/\+\-.()]+", equation_string)
    filtered_eq = ''.join(equation_string)
    return filtered_eq


def calculation(filtered_equation):
    # Calculates the answer
    operators = re.findall("[*%/\+\-]+", filtered_equation)
    try:
        answer = eval(filter(filtered_equation))
        return answer
    except SyntaxError:
        return "You have used too many operators, decimal points or numbers starting with zero. Please try again."


# Input string
input_equation = input("Insert your equation here:")

print(calculation(input_equation))
