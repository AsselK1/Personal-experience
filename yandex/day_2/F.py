n = int(input())
nums = list(map(int, input().split()))
i = 0
start = 0
while i < n:
    if nums[i] == nums[-1]:
        start = i
        end = -2
        while n - 1 > i > end and nums[i + 1] == nums[end]:
            i += 1
            end -= 1
        if i==end or i==n-1:
            break
    i += 1
ans = []
for j in range(start - 1, -1, -1):
    ans.append(str(nums[j]))

print(len(ans))
print(' '.join(ans))
