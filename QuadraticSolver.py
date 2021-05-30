import math


# Generates real and complex solutions for a quadratic polynomial
def solution(var_a, var_b, to_root):
    if to_root > 0:
        sol_1 = (-1 * var_b + math.sqrt(to_root)) / (2 * var_a)
        sol_2 = (-1 * var_b - math.sqrt(to_root)) / (2 * var_a)
        print(f"The solutions are:\n{sol_1}\n{sol_2}")
    elif to_root == 0:
        sol_rep = (-1 * var_b + math.sqrt(to_root)) / (2 * var_a)
        print(f"The solution to this quadratic equation is:\n{sol_rep}")
    else:
        real_coefficient = (-1 * var_b) / (2 * var_a)
        complex_coefficient_1 = math.sqrt(-1 * to_root) / (2 * var_a)
        complex_coefficient_2 = -(1 * math.sqrt(-1 * to_root)) / (2 * var_a)
        sol_com_1 = complex(real_coefficient, complex_coefficient_1)
        sol_com_2 = complex(real_coefficient, complex_coefficient_2)
        print(f"The solutions are:\n{sol_com_1}\n{sol_com_2}")


# Coefficients of the polynomial
a = float(
    input("Welcome to this polynomial solver. Please place in the coefficients of your quadratic where appropriate.\n"
          "This is in the format of ax^2 + bx + c = 0. Enter the coefficients as required below.\n a:"))
b = float(input("b:"))
c = float(input("c:"))

# Test to determine whether real or complex roots are generated
root_sol = b ** 2 - 4 * a * c

# Calls the function
solution(a, b, root_sol)
