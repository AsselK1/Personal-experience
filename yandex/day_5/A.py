a = int(input())
b = list(map(int, input().split()))

c = int(input())
d = list(map(int, input().split()))


def clothes(n, l, m, g, p1, p2):
    ans = [l[p1], g[p2]]
    max_ = float('inf')
    while p1 < n and p2 < m:
        if l[p1] == g[p2]:
            return str(l[p1]) + ' ' + str(g[p2])
        elif l[p1] > g[p2]:
            if l[p1] - g[p2] < max_:
                max_ = l[p1] - g[p2]
                ans = [l[p1], g[p2]]
            p2 += 1

        else:
            if -l[p1] + g[p2] < max_:
                max_ = g[p2] - l[p1]
                ans = [l[p1], g[p2]]
            p1 += 1
    return ' '.join(str(v) for v in ans)


print(clothes(a, b, c, d, 0, 0))
