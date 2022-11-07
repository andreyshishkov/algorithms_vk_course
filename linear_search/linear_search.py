n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

curr_max = 0
maximums = []
for i in range(n):
    if A[i] > A[curr_max]:
        curr_max = i
    maximums.append(curr_max)

first = second = 0
max_ = B[0] + A[maximums[0]]
for i in range(n):
    curr_max = B[i] + A[maximums[i]]
    if curr_max > max_:
        max_ = curr_max
        first = maximums[i]
        second = i

print(first, second)