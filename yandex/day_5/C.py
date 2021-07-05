n = int(input())
right = [0,0]
wrong = [0,0]
a = list(map(int, input().split()))
prev = a[1]
for _ in range(n-1):
    x = list(map(int, input().split()))
    if x[1] > prev:
        right.append(right[-1] + x[1] - prev)
        wrong.append(wrong[-1])
    elif x[1] < prev:
        wrong.append(wrong[-1] + prev - x[1])
        right.append(right[-1])
    else:
        wrong.append(wrong[-1])
        right.append(right[-1])
    prev = x[1]

m = int(input())
for _ in range(m):
    x = list(map(int, input().split()))
    if x[1] > x[0]:
        print(right[x[1]]-right[x[0]])
    elif x[0] > x[1]:
        print(wrong[x[0]]-wrong[x[1]])
    else:
        print(0)

