def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


class Point:

    def __init__(self, x: int, start: bool = False):
        self.x = x
        self.start = start

    def __eq__(self, other):
        return self.x == other.x

    def __le__(self, other):
        return self.x <= other.x

    def __gt__(self, other):
        return self.x > other.x


if __name__ == '__main__':
    n = int(input())
    points = []

    for _ in range(n):
        l, r = [int(x) for x in input().split()]
        points.append(Point(l, True))
        points.append(Point(r))

    merge_sort(points)

    result = 0
    cur_layers = 0
    last_start = -1

    for i in range(2 * n):
        was_1 = cur_layers == 1

        cur_layers += 1 if points[i].start else -1

        if cur_layers == 1:
            last_start = points[i].x
        elif was_1:
            result += points[i].x - last_start

    print(result)
