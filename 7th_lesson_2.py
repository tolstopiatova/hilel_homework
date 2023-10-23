import random
# Створюємо словник з 20 випадковими числами
random_dict = {}
for i in range(21):
    random_dict[i] = random.randint(0, 100)

# Обчислюємо добуток всіх значень словника
product = 1
for value in random_dict.values():
    product *= value

# Виводимо словник та результат множення
print("Згенерований словник:", random_dict)
print("Результат множення чисел у словнику:", product)