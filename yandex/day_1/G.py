a = list(map(int, input().split()))
n = a[0]
k = a[1]
m = a[2]

z = 0
d = 0
if m<=k:
    while n >= k:
        z = n // k
        n %= k
        d += (k // m) * z
        n += (k % m) * z
print(d)
