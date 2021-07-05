import time
start_time = time.time()
n = int(input())
point = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    point.append([x,y])
total=0
for i in range(n):
    hs = set()
    hm = {}
    x0 = point[i][0]
    y0 = point[i][1]
    for j in range(n):
        x = x0 - point[j][0]
        y = y0 - point[j][1]
        if (x0+x, y0+y) in hs:
            total-=1
        else:
            hs.add((point[j][0],point[j][1]))
        d = x**2+y**2
        if d in hm:
            hm[d]+=1
            a=hm[d]
            total+=a-1
        else:
            hm[d]=1
print(total)
print("--- %s seconds ---" % (time.time() - start_time))
