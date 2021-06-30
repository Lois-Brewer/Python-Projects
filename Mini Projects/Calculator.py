operator_list = ['+', '-', '*', '/', '%', '**', '^', '//']

equation = input("Insert your equation here:")

contains_operator = any(operator in equation for operator in operator_list)
print(contains_operator)

if contains_operator:
    answer = eval(equation)
    print(answer)
else:
    print("Numbers and operators only!")
