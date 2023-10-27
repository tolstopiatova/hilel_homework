import random
# Генеруємо список int_elements з 25 чисел в діапазоні від 1 до 500
int_elements = [random.randint(1, 500) for i in range(25)]

# Виводимо список int_elements
print("int_elements:", int_elements)

# Список, що складається із квадратів int_elements
squares = [x ** 2 for x in int_elements]
print("Список квадратів: ", squares)

# Список, що складається із остач ділення на 11 елементів 
mod_11 = [x % 11 for x in int_elements]
print("Список остач ділення на 11 елементів: ", mod_11)

# Список, що складається лише з парних елементів int_elements
even_elements = [x for x in int_elements if x % 2 == 0]
print("Список парних елементів: ", even_elements)

# Список, що складається лише з елементів  з непарною кількістю цифр
odd_digit_count = [x for x in int_elements if len(str(x)) % 2 != 0]
print("Список елементів з непарною кількістю цифр: ", odd_digit_count)

# Список, що складається з елементів позиція яких не є кратними 3
not_multiple_of_3 = [x for i, x in enumerate(int_elements) if i % 3 != 0]
print("Список елементів, що не є кратними 3: ", not_multiple_of_3)