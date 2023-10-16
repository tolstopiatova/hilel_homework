numbers = []
i = 0
while True:
    number = int(input("Введіть число N: "))
    if number == 0:
        break
    numbers.append(number)
    print(numbers)
    i += 1
#Сумму чисел
summa = 0
for element in numbers:
    summa += element
print('сума ', summa)
#Середнє арифметичне усіх введених чисел (не враховуючи останнього 0)
print('середнє ', summa/len(numbers))
#Визначити максимальне і мінімальне занчення
print('max_value ', max(numbers))
print('min_value ', min(numbers))
#Визначити кількість парних та кількість не парних чисел
parni = []
neparni = []
for element in numbers:
    if element % 2 == 0:
        parni.append(element)
    else:
        neparni.append(element)
print('парних ', len(parni))
print ('непарних ', len(neparni))