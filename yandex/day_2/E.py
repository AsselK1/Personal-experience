n = int(input())
distances = list(map(int, input().split()))
winner = distances[0]
curr_len = 0
for i in range(1, len(distances)):
    if distances[i] > winner:
        winner = distances[i]
        curr_len = 0
    else:
        if i < len(distances) - 1 and distances[i] > distances[i + 1] and distances[i] % 10 == 5 and distances[i] > curr_len:
            curr_len = distances[i]

curr = 1
if curr_len == 0:
    print(0)
else:
    for i in range(len(distances)):
        if distances[i] > curr_len:
            curr += 1
    print(curr)
