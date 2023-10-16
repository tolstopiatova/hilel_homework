N = int(input("Введіть число N: "))

i = 1
while i <= N:
    count = i * i
    #count_str = str(count)
    if str(i) == str(count)[-len(str(i)):]:
       # print(str(count)[-len(str(i)):])
        if i <= N:
            print(i, '*', i, '=', i*i)
    i += 1