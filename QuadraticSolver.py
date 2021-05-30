import math


# Generates real and complex solutions for a quadratic polynomial
def solution(var_a, var_b, to_root):
    if to_root > 0:
        sol_1 = (-1 * var_b + math.sqrt(to_root)) / (2 * var_a)
        sol_2 = (-1 * var_b - math.sqrt(to_root)) / (2 * var_a)
        return f"The solutions are:\n{sol_1}\n{sol_2}"
    elif to_root == 0:
        sol_1 = (-1 * var_b + math.sqrt(to_root)) / (2 * var_a)
        return f"The solution to this quadratic equation is:\n{sol_1}"
    else:
        real_coefficient = (-1 * var_b) / (2 * var_a)
        complex_coefficient_1 = math.sqrt(-1 * to_root) / (2 * var_a)
        complex_coefficient_2 = -(1 * math.sqrt(-1 * to_root)) / (2 * var_a)
        sol_1 = complex(real_coefficient, complex_coefficient_1)
        sol_2 = complex(real_coefficient, complex_coefficient_2)
        return f"The solutions are:\n{sol_1}\n{sol_2}"


print("Welcome to this polynomial solver. Please place in the coefficients of your quadratic where appropriate.\n"
      "This is in the format of ax^2 + bx + c = 0. Enter the coefficients as required below.")

# Coefficients of the polynomial
a = input("a:")
b = input("b:")
c = input("c:")

check_numeric = all((a.isnumeric(), b.isnumeric(), c.isnumeric()))

if check_numeric:
    a, b, c = float(a), float(b), float(c)
    root_sol = b ** 2 - 4 * a * c

    print(solution(a, b, root_sol))
else:
    print("You can only insert numbers.")
