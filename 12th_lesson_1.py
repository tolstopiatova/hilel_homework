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
    for j in range(n):
        for i in range(n - 1):
                for k in range(n - 1 - i):
                    if (((j+1) % 2 ==1 and matrix[k][j] < matrix [k+1][j]) or
                        ((j+1) % 2 ==0 and matrix[k][j] > matrix [k+1][j])):
                          matrix[k][j], matrix[k+1][j] = matrix[k+1][j], matrix[k][j]
    return matrix


def print_matrix(matrix):
    max_elem_len = 2  

    sums = [0] * len(matrix[0])
    for row in matrix:
        for i, elem in enumerate(row):
            sums[i] += elem
            print(f"{elem:>{max_elem_len}}", end=" ")
        print()

    for col_sum in sums:
        print(f"{col_sum:>{max_elem_len}}", end=" ")
    print()


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
