sizes = list(map(int, input().split()))
a = sizes[0]
b = sizes[1]
c = sizes[2]
d = sizes[3]
min_area = (a + c) * max(b, d)
size1 = a + c
size2 = max(b, d)
if min_area > (a + d) * max(b, c):
    size1 = a + d
    size2 = max(b, c)
    min_area=(a + d) * max(b, c)
if min_area > (b + c) * max(a, d):
    size1 = b + c
    size2 = max(a, d)
    min_area=(b + c) * max(a, d)
if min_area > (b + d) * max(a, c):
    size1 = b + d
    size2 = max(a, c)
    min_area=(b + d) * max(a, c)
print(str(size1) + ' ' + str(size2))
