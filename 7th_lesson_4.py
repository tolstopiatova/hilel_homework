# Два списки
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
# Створення порожнього словника
result_dict = {}
# Заповнення словника за допомогою циклу
for i in range(len(keys)):
    result_dict[keys[i]] = values[i]
# Виведення створеного словника
print(result_dict)