import random

# Генеруємо множину з 15 випадкових чисел
random_numbers = set(random.randint(1, 100) for _ in range(15))

# Розділяємо числа на парні і непарні
even_numbers = {num for num in random_numbers if num % 2 == 0}
odd_numbers = random_numbers - even_numbers

# Обчислюємо суми парних і непарних чисел
sum_even = sum(even_numbers)
sum_odd = sum(odd_numbers)

# Визначаємо результат
if sum_odd > sum_even:
    result = "Так"
else:
    result = "Ні"

# Виводимо результат
print("Множина випадкових чисел:", random_numbers)
print("Сума непарних чисел:", sum_odd)
print("Сума парних чисел:", sum_even)
print("Результат (Так/Ні):", result)