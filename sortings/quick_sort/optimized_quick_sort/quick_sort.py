def get_pivot(array: list[int]) -> int:
    return array[-1]


def partition(array, low, high):
    pivot = get_pivot(array[low: high + 1])

    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1

            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def insert_sort(array: list[int], low, high):
    for i in range(low + 1, high + 1):
        tmp = array[i]
        j = i - 1
        while j >= 0 and tmp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp
    return array


def quick_sort(array: list[int], low, high) -> list[int]:
    if low >= high:
        return
    if high - low > 40:
        pivot = partition(array, low, high)

        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)
    else:
        insert_sort(array, low, high)


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    n = len(nums)
    quick_sort(nums, 0, n - 1)
    print(*nums[9::10])
