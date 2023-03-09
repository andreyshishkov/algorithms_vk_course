class Heap:

    def __init__(self, arr=None):
        self._arr = arr if arr is not None else []
        self.build_heap()

    def sift_up(self, index: int):
        assert index < len(self._arr)
        while index > 0:
            parent = (index - 1) // 2
            if self._arr[index] <= self._arr[parent]:
                return
            self._arr[parent], self._arr[index] = self._arr[index], self._arr[parent]
            index = parent

    def sift_down(self, index):
        assert index < len(self._arr)
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self._arr) and self._arr[left] > self._arr[index]:
            largest = left
        if right < len(self._arr) and self._arr[right] > self._arr[largest]:
            largest = right
        if largest != index:
            self._arr[index], self._arr[largest] = self._arr[largest], self._arr[index]
            self.sift_down(largest)

    def add(self, elem):
        self._arr.append(elem)
        self.sift_up(len(self._arr) - 1)

    def build_heap(self):
        n = len(self._arr) // 2 - 1
        for i in range(n, -1, -1):
            self.sift_down(i)

    def get_max(self):
        assert len(self._arr) > 0
        result = self._arr[0]
        self._arr[0] = self._arr[-1]
        del self._arr[-1]
        if len(self._arr) > 0:
            self.sift_down(0)
        return result

    def check_max(self):
        return self._arr[0]

    def __bool__(self):
        return len(self._arr) > 0


amount = int(input())
weights = [int(x) for x in input().split()]
k_max = int(input())

weight_heap = Heap(weights)
count = 0
total_weight = 0
tmp = []
while True:
    cur_weight = weight_heap.check_max() if weight_heap else 0
    if weight_heap and total_weight + cur_weight <= k_max:
        total_weight += weight_heap.get_max()
        if cur_weight != 1:
            tmp.append(cur_weight // 2)
    else:
        while tmp:
            weight_heap.add(tmp.pop())
        total_weight = 0
        count += 1

    if not weight_heap and not tmp:
        count += 1
        break

print(count)
