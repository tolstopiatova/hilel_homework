# Тестовий список
test_list = [1, 2, "hello", [3, 4], (5, 6), {"name": "John", "age": 30}]
result_set = set()
# Перебираємо елементи списку
for item in test_list:
    try:
        # Додаємо елемент до множини, якщо він може бути хешований
        result_set.add(item)
    except TypeError:
        pass
print("Множина без неможливих до хешування об'єктів:")
print(result_set)
