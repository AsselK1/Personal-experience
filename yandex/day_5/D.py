x = list(map(int, input().split()))
n = x[0]
k = x[1]
d = list(map(int, input().split()))

start = 0
end = 1
count = 0
while start < n - 1:
    while end < n and d[end] - d[start] <= k:
        end += 1
    if end == n:
        break
    else:
        count += n - end
        start += 1

print(count)
