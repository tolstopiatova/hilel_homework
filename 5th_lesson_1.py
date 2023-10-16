N = input('input number:  ')
list_N = list(N)
length = len(list_N)
print (list_N, length)
has_duplicate = False

i = 0
while i < length:
    j = 0
    while j < length:
        if list_N[i] == list_N[j] and i != j:
            has_duplicate = True
            break
        j = j + 1
    if has_duplicate:
        break
    i = i + 1
if has_duplicate:
    print('yes')
else:
    print('No')
