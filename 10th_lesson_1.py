def has_pair_with_sum(arr, target_sum):
    seen = set()
    for number in arr:
        complement = target_sum - number
        if complement in seen:
            return True
        seen.add(number)
    return False

arr1 = [1, 2, 3, 4, 5]
target_sum1 = 7
result1 = has_pair_with_sum(arr1, target_sum1)
print(f"У списку arr1 є пара чисел з сумою {target_sum1}: {result1}")

arr2 = [10, 15, 20, 25]
target_sum2 = 90
result2 = has_pair_with_sum(arr2, target_sum2)
print(f"У списку arr2 є пара чисел з сумою {target_sum2}: {result2}")
