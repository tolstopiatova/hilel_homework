def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_generator(n, z):
    for num in range(n, z + 1):
        if is_prime(num):
            yield num

# Вибираємо випадкові значення для n та z
import random
n = random.randint(1, 100)
z = random.randint(101, 200)

print(f"Прості числа у діапазоні від {n} до {z}:")
prime_numbers = list(prime_generator(n, z))
print(" ".join(map(str, prime_numbers)))
