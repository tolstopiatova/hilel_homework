N = input('введіть рядок з 15 символів: ')
if len(N) == 0:
    print('рядок пустий, роботу буде завершено')
elif len(N) < 15:
    N=(N*3)
if len(N) >= 15:
    b = list(N)
#вивести повний список
    print(b)
#вивести зі списку остaнні 5 елементів
    print(b[(len(b)-5):len(b)])
#вивести список (зеркально обернено) в зворотній послідовності
    print(b[::-1])
#вивести список усіх  елементів з парними індексами
    print(b[::2])
#вивести список у якому 5 елементів спочатку такі ж самі як остані 5 елементів списку
    b[0:5] = b[(len(b)-5):len(b)]
    print(b)