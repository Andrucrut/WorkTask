import itertools


numbers = list(range(3, 12))
squares = itertools.permutations(numbers, 9)

def check(args):
    row_products = [row[0] * row[1] * row[2] for row in args]
    col_products = [col[0] * col[1] * col[2] for col in zip(*args)]
    return all(row_products[i] == col_products[i] for i in range(3))


for square in squares:
    matrix = [square[i:i+3] for i in range(0, 9, 3)]
    if check(matrix):
        for row in matrix:
            print(row)
        break
else:
    print("Not found")



