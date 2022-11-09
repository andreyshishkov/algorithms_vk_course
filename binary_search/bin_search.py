def find_indexes(n: int, a: list[int], b: list[int]) -> list[int]:
    indexes = []
    for b_i in b:

        # поиск окрестности в близи значения 2-го массива
        start_pos = 0
        end_pos = 2
        while end_pos < n:
            if a[end_pos] > b_i:
                break
            start_pos = end_pos
            end_pos *= 2
        end_pos = n if end_pos >= n else end_pos

        # выполняем поиск ближайшего элемента
        while start_pos < end_pos:
            middle = (start_pos + end_pos) // 2

            if a[middle] > b_i:
                end_pos = middle
            elif a[middle] < b_i:
                start_pos = middle + 1
            else:
                start_pos = end_pos = middle
                break

        if start_pos not in (0, n):
            start_pos -= 1
            start_pos = end_pos if abs(a[start_pos] - b_i) > abs(a[end_pos] - b_i) else start_pos

        elif start_pos == n:
            start_pos = n - 1

        indexes.append(start_pos)

    return indexes


if __name__ == '__main__':
    N = int(input())
    A = [int(x) for x in input().split()]

    M = int(input())
    B = [int(x) for x in input().split()]

    result = find_indexes(N, A, B)
    print(*result)
