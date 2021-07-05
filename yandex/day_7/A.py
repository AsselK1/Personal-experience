n, m = list(map(int, input().split()))
teachers = []
for _ in range(m):
    start, end = list(map(int, input().split()))
    teachers.append((start, -1))
    teachers.append((end, 1))
teachers.sort()
watched = 0
total=0
total+=teachers[0][0]
watched=1
for i in range(1, len(teachers)):
    if watched == 0:
        total+=teachers[i][0] - teachers[i-1][0] - 1
    watched -= teachers[i][1]
total+=n-teachers[-1][0]-1
print(total)
    

