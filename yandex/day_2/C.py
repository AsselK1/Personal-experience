dif = 2001
n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
for i in range(len(numbers)):
    if abs(numbers[i] - target) < dif:
        ans = numbers[i]
        dif=abs(numbers[i] - target)
print(ans)
