import random


def create_matrix(M):
    """ Функція для створення випадкового двовимірного списку розміром MxM """
    return [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]


def bubble_sort_and_sum(matrix):
    """визначення суми"""
    sums = [0] * len(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sums[j] += matrix[i][j]
    n = len(sums)
    """виправлене сортування"""
    for i in range(n):
        for j in range(0, n - i - 1):
            if sums[j] > sums[j + 1]:
                sums[j], sums[j + 1] = sums[j + 1], sums[j]
                for k in range(len(matrix)):
                    matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]
    return matrix


def print_matrix(matrix):
    """виведення матриці на екран"""
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

        sorted_matrix = bubble_sort_and_sum(matrix)
        print("\nВідсортована матриця:")
        print_matrix(sorted_matrix)
