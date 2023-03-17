def get_partition(array, low, high):
    pivot = array[high]
    pivot_ind = low

    for i in range(low, high):
        if array[i] <= pivot:
            array[i], array[pivot_ind] = array[pivot_ind], array[i]
            pivot_ind += 1

    array[high], array[pivot_ind] = array[pivot_ind], array[high]
    return pivot_ind


def get_k_order_stat(array, low, high, k):
    pivot_ind = get_partition(array, low, high)

    if pivot_ind - low == k:
        return array[pivot_ind]

    elif pivot_ind - low > k:
        return get_k_order_stat(array, low, pivot_ind - 1, k)
    else:
        return get_k_order_stat(array, pivot_ind + 1, high, k - pivot_ind + low - 1)


def main():
    n, k = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]

    result = get_k_order_stat(array, 0, n - 1, k)
    print(result)


if __name__ == '__main__':
    main()
