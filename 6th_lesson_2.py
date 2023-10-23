number = int(input('Input number: '))

for i in range(number):
    a = 10 ** i
    num_zeros = number - i + 1
    row = f"{i:2}:{' ' * num_zeros}{a}"
    print(row)