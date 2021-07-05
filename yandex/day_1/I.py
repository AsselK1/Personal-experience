a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a <= 0 or b <= 0 or c <= 0 or d <= 0 or e <= 0:
    print("NO")
else:
    if a <= b <= c:
        x = a
        y = b
    if b <= a <= c:
        x = b
        y = a
    if a <= c <= b:
        x = a
        y = c
    if c <= a <= b:
        x = c
        y = a
    if c <= b <= a:
        x = c
        y = b
    if b <= c <= a:
        x = b
        y = c
    if x<=min(d, e) and y<=max(d, e):
        print("YES")
    else:
        print("NO")
