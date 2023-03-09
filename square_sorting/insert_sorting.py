def insert_sort(array):
    for i in range(1, len(array)):
        tmp = array[i]
        j = i - 1
        while j >= 0 and tmp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp
    return array


arr = [int(x) for x in input().split()]
sorted_arr = insert_sort(arr)
print(*sorted_arr)
