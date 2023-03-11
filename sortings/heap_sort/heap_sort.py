import heapq


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        if self.x != other.x:
            return self.x > other.x

        return self.y > other.y

    def __str__(self):
        return f'{self.x} {self.y}'


n = int(input())
points = []
for _ in range(n):
    x, y = [int(i) for i in input().split()]
    points.append(Point(x, y))

heapq.heapify(points)
sorted_arr = []
for _ in range(n):
    elem = heapq.heappop(points)
    sorted_arr.append(elem)

for point in sorted_arr:
    print(point)
