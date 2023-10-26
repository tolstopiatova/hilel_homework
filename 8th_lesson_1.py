# Вхідний список чисел
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
# Створюємо множину, щоб видалити дублікати
unique_numbers = set(numbers)
# Знаходимо кількість різних чисел
count_unique = len(unique_numbers)
print("Кількість різних чисел у списку:", count_unique)