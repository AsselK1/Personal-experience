t,d,n=list(map(int, input().split()))
hor1_0 = 0
hor2_0 = 0
ver1_0 = 0
ver2_0 = 0
for _ in range(n):
    x,y = list(map(int, input().split()))
    hor1_0 +=t
    hor2_0 -=t
    ver1_0 +=t
    ver2_0 -=t
    hor1 = x+y+d
    hor2 = x+y-d
    ver1 = y-x+d
    ver2 = y-x-d
    hor1_0 = min(hor1_0, hor1)
    hor2_0 = max(hor2_0, hor2)
    ver1_0 = min(ver1_0, ver1)
    ver2_0 = max(ver2_0, ver2)
for i in range(hor2_0, hor1_0+1):
    for j in range(ver2_0, ver1_0+1):
        if i%2!=j%2:
            continue
        x = (i-j)//2
        y = (i+j)//2
        print(str(x)+' '+str(y))
