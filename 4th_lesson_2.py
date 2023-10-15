#A
first = (1,2,3)
print(type(first))
second = (3,4,5)
print(type(second))
print(first,second)
a = list(first)
b = list(second)
result = a + b
print(result)
print(type(result))
#B
print(a, b)
a.reverse()
a1 = tuple(a)
b.reverse()
b1 = tuple(b)
print(a1, b1)
t_result = (result, a1, b1)
print(t_result)
#C
#result_2 = t_result[0][2]
print(t_result[0][2], t_result[1][2], t_result[2][2])