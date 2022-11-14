def factorization(n):
    n1 = n
    i = 2
    prims = []
    while i * i < n1:
        while n % i == 0:
            n //= i
            prims.append(i)
        i += 1
    if n != 1:
        prims.append(n)
    return prims


num = int(input())
if num > 1:
    print(*factorization(num))
