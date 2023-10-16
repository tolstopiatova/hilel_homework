N = int(input('input number: '))
i = 0
while i < N:
    count = i * i
    if count < N:
        print(i, '*', i, '=', i*i)
    i += 1