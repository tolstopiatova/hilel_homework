import random
import pprint
number = int(input('введіть розмір матриці: '))
matrix = [[random.randint(1, 100) for _ in range(number)] for __ in range(number)]
pprint.pprint(matrix)
diagonal_sum = sum(matrix[i][i] for i in range(number))
print("сума по діагоналі:", diagonal_sum)
summa_col = sum(matrix[i][number - 1] for i in range(number))
print("сума ", number, "стовбця", summa_col)
