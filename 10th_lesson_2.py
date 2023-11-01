import random

# Функція для генерації 2-вимірного списку
def generate_2d_list(rows=3, cols=3):
    return [[random.randint(0, 200) for _ in range(cols)] for _ in range(rows)]

# Функція для виведення симетричної таблиці
def print_symmetric_table(table):
    if not all(len(row) == len(table[0]) for row in table):
        print("Неможливо надрукувати симетричну таблицю, оскільки розміри рядків відрізняються.")
    else:
        max_width = max(max(len(str(value)) for value in row) for row in table)
        for row in table:
            print(" | ".join(str(value).rjust(max_width) for value in row))

# Виведення таблиць залежно від кількості параметрів для першої функції
table1 = generate_2d_list()
table2 = generate_2d_list(4)
table3 = generate_2d_list(4, 5)

print("Таблиця 1 (без параметрів):")
print_symmetric_table(table1)

print("\nТаблиця 2 (з одним параметром):")
print_symmetric_table(table2)

print("\nТаблиця 3 (з двома параметрами):")
print_symmetric_table(table3)
