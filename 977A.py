n, k = input().split()
n = int(n)
k = int(k)
while k != 0:
    if n % 10 == 0:
        n = n // 10
    else:
        n = n - 1
    k -= 1
print(n)
