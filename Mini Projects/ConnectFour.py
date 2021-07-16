# As per matrices - rows go across and columns go down
COLUMN_COUNT = 7
ROW_COUNT = 6

grid = [['-'] * COLUMN_COUNT] * ROW_COUNT

for row in grid:
    print(*row)
