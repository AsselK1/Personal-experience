a = int(input())
b = int(input())
n = int(input())
m = int(input())
if n == 0:
    t1 = 0
else:
    t1 = n + a * (n - 1)
t2 = n + a * (n + 1)
if m == 0:
    t3 = 0
else:
    t3 = m + b * (m - 1)
t4 = m + b * (m + 1)
if max(t1, t3) <= min(t2, t4):
    print(max(t1, t3), min(t2, t4))
else:
    print(-1)
