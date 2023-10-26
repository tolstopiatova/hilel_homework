# Вхідні списки чисел
list1 = [1, 2, 2, 3, 4, 5, 19, 123]
list2 = [2, 3, 4, 4, 5, 6, 21, 3589]
# Створюємо множини
set1 = set(list1)
set2 = set(list2)
# Знаходимо співпадіння та не співпадіння
common_numbers = set1 ^ set2
diff_numbers = set1 & set2
# Знаходимо кількість різних чисел, які є в обох списках
count_common = len(common_numbers)
count_diff = len(diff_numbers)
count_numbers = count_common + count_diff
print("числа:", common_numbers, diff_numbers )
print("Кількість різних чисел в обох списках:", count_numbers)