# As per matrices - rows go across and columns go down
COLUMN_COUNT = 7
ROW_COUNT = 6
boolean = True

grid = [['-'] * COLUMN_COUNT] * ROW_COUNT


def print_grid(new_grid):
    for s in new_grid:
        print(*s)


print_grid(grid)
