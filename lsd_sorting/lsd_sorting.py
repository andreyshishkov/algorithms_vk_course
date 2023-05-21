def int_to_bytes(num: int):
    byte_arr = num.to_bytes(8, byteorder='big')
    return byte_arr


def counting_sort(arr, byte_num):
    n = len(arr)

    c = [0 for _ in range(256)]
    for number in arr:
        byte_val = int_to_bytes(number)[byte_num]
        c[byte_val] += 1

    for i in range(1, 256):
        c[i] += c[i - 1]

    b = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        tmp = int_to_bytes(arr[i])[byte_num]
        c[tmp] -= 1
        b[c[tmp]] = arr[i]
    return b


def lsd_sort(arr, len_r=8):
    for i in range(len_r - 1, -1, -1):
        arr = counting_sort(arr, i)

    return arr


def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]

    result = lsd_sort(numbers)
    print(*result)


if __name__ == '__main__':
    main()
