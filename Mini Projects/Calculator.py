import re


def filter(equation_string):
    # Filters input string to an equation
    equation_string = re.findall("[0-9^*%/\+\-.()]+", equation_string)
    filtered_eq = ''.join(equation_string)
    return filtered_eq


def calculation(filtered_equation):
    # Calculates the answer
    for i in range(len(filtered_equation)):
        try:
            answer = eval(filter(filtered_equation))
            return answer
        except filtered_equation[i] == '0' and SyntaxError:
            filtered_equation = filtered_equation.replace(str(i), '')
            return eval(filter(filtered_equation))
    print(filtered_equation)



# Input string
input_equation = input("Insert your equation here:")

print(calculation(input_equation))
