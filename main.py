# Using nested loops to print a rectangle in Python

num_rows = 2

num_cols = 3

for i in range(num_rows):
    for i in range(num_cols):
        print('*', end=' ')
    print('')