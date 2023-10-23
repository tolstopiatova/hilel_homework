# Генеруємо словник, де ключами є числа від 1 до 10, а значеннями їх куб
cubed_dict = {}
for i in range(1, 11):
    cubed_dict [i] = {i * i * i}

# Виводимо згенерований словник
print(cubed_dict.keys())
print(cubed_dict.values())