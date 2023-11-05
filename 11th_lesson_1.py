import math
# Анонімна функція для обчислення гіпотенузи прямокутного трикутника
hypotenuse = lambda x, y=1:math.sqrt(x*x + y*y)

# Приклад 1: передається один список чисел для обробки в map
numbers = [ (3, 4), (5, 12), (8, 15) ]
result = list(map(lambda xy: hypotenuse(*xy), numbers))
print(result)

# Приклад 2: передається два списки чисел для обробки в map
x_values = [3, 5, 8]
y_values = [4, 12, 15]
result = list(map(hypotenuse, x_values, y_values))
print(result)
