k = int(input())
word = input()
n = len(word)
l = n-1
ways = 0
prev = 0
while l >= k:
    r = l - k
    if word[r] == word[l]:
        prev += 1
        ways += prev
    else:
        prev = 0
    l -= 1
print(ways)
