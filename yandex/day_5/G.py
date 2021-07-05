n, k = list(map(int, input().split()))
scores = list(map(int, input().split()))
hscore = {}
for i in range(len(scores)):
    hscore[scores[i]] = hscore.get(scores[i], 0) + 1
scores = sorted(hscore)
l = 0
r = 0
total = 0
count = 0
while l < len(scores):
    while r < len(scores) and scores[r] <= scores[l] * k:
        if hscore[scores[r]] >= 2:
            count += 1
        r += 1
    if hscore[scores[l]] >= 2:
        count -= 1
        total += (r - l - 1) * 3
        if hscore[scores[l]] >= 3:
            total += 1
    total += (r - l - 1) * (r - l - 2) * 3
    total += count * 3
    l += 1
print(total)
