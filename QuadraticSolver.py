def if_real_solution(root):
    if root < 0:
        print("This will have a complex solution.")
    elif root == 0:
        print("This solution will have a repeated root.")
    else:
        print("This solution will have two distinct roots.")
    print(root)

a = input("Welcome to this polynomial solver. Please place in the coefficients of your quadratic where appropriate.\n"
          "This is in the format of ax^2 + bx + c = 0. Enter the coefficients as required below.\n a:")
b = input("b:")
c = input("c:")

d = 4 * int(a) * int(c)
e = int(b) ** 2
square_root = d-e

if_real_solution(square_root)
