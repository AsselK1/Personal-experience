x = list(map(int, input().split()))
a = x[0]
b = x[1]
c = list(map(int, input().split()))


def f(n, k, d):
    hm_f = {}
    start = -1
    end = -1
    while len(hm_f) < k:
        end += 1
        hm_f[d[end]] = hm_f.get(d[end], 0) + 1
    ans = end + 1
    ind = [0, end]
    while start <= end < n and start < n-1:
        if ans == k:
            return ' '.join(str(v + 1) for v in ind)
        start += 1
        if hm_f[d[start]] - 1 > 0:
            hm_f[d[start]] -= 1
            if ans >= end - start:
                ans = end - start
                ind = [start + 1, end]
        else:
            end += 1
            while end < n and d[end] != d[start]:
                hm_f[d[end]] += 1
                end += 1
            if end == n:
                return ' '.join(str(v + 1) for v in ind)


print(f(a, b, c))
