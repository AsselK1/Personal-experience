x = list(map(int, input().split()))
n = x[0]
k = x[1]

m = list(map(int, input().split()))
hm = {0: 1}
summ = 0
for i in range(len(m)):
    summ += m[i]
    hm[summ] = hm.get(summ, 0) + 1
count = 0
for i in hm:
    if i >= k:
        if i-k in hm:
            count += 1

print(count)
