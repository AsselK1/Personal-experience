n, k = list(map(int, input().split()))
word = input()
l = 0
r = 0
leng = -1
ans = None
hm = {}
while l < n:
    while r < n and hm.get(word[r], 0) < k:
        hm[word[r]] = hm.get(word[r], 0) + 1
        r += 1
    if leng < r - l:
        leng = r - l
        ans = l
    if r == n:
        break
    else:
        while word[l] != word[r]:
            hm[word[l]] -= 1
            l += 1
    hm[word[l]] -= 1
    l += 1
print(str(leng) + ' ' + str(ans + 1))
