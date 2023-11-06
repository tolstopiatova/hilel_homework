import random

# Функція для створення випадкового двовимірного списку розміром MxM
def create_matrix(M):
    return [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]

# Функція для сумування елементів стовпців і сортування
def sort_matrix(matrix):
    sums = [sum(col) for col in zip(*matrix)]
    sorted_indices = sorted(range(len(sums)), key=lambda i: sums[i])

    for i in range(len(matrix)):
        if i % 2 == 0:
            matrix[i] = sorted(matrix[i])
        else:
            matrix[i] = sorted(matrix[i], reverse=True)

    sorted_matrix = [list(row) for row in zip(*matrix)]
    return sorted_matrix

# Функція для виведення матриці на екран
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    sums = [sum(col) for col in zip(*matrix)]
    print("Суми стовпців:", sums)

# Головна частина програми
if __name__ == "__main__":
    M = int(input("Введіть розмір матриці (MxM), M > 5: "))
    if M <= 5:
        print("Розмір матриці має бути більшим за 5.")
    else:
        matrix = create_matrix(M)
        print("Початкова матриця:")
        print_matrix(matrix)

        sorted_matrix = sort_matrix(matrix)
        print("\nВідсортована матриця:")
        print_matrix(sorted_matrix)
