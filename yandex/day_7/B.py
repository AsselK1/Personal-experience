n, m = list(map(int, input().split()))
lines = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    lines.append((x,-1))
    lines.append((y, 1))
points = input().split()
for point in points:
    lines.append((int(point),0))
lines.sort()
ans = {}
count=0
for i in range(len(lines)):
    if lines[i][1]==-1:
        count+=1
    elif lines[i][1]==1:
        count-=1
    else:
        ans[lines[i][0]] = count
a = []
for point in points:
    a.append(str(ans[int(point)]))
print(' '.join(a))