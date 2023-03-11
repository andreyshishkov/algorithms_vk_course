import heapq


class Element:

    def __init__(self, array_index, elem_index, arrays):
        self.array_index = array_index
        self.elem_index = elem_index
        self.arrays = arrays

    @property
    def value(self):
        return self.arrays[self.array_index][self.elem_index]

    @value.setter
    def value(self, v):
        self.arrays[self.array_index][self.elem_index] = v

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value


def merge_k_sorted(arrays):
    result = []
    min_heap = []

    for i, array in enumerate(arrays):
        a = Element(i, 0, arrays)
        min_heap.append(a)
    heapq.heapify(min_heap)

    while min_heap[0].value != float('+inf'):
        top = min_heap[0]
        result.append(top.value)
        #top.elem_index += 1

        if (top.elem_index + 1) >= len(arrays[top.array_index]):
            top.value = float('+inf')
        else:
            top.elem_index += 1

        heapq.heapify(min_heap)

    return result


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())

    sub_arrays = [[arr[i], arr[i + k]] for i in range(n - k)]
    sorted_array = merge_k_sorted(sub_arrays)
    print(*sorted_array)
