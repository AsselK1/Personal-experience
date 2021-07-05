def find_P_and_N(k1, m, k2, p2, n2):
    if n2 > m:
        return '-1 -1'
    if n2 == 1:
        if p2 == 1:
            if k1 <= k2:
                return '1 1'
            else:
                if m * k2 >= k1:
                    return '1 0'
                elif m == 1:
                    return '0 1'
                else:
                    return '0 0'
    if k2 % (m * (p2 - 1) + n2) == 0:
        less1 = k2 // (m * (p2 - 1) + n2)
    else:
        less1 = k2 // (m * (p2 - 1) + n2) + 1
    if k2 % (m * (p2 - 1) + n2 - 1) == 0:
        larger1 = k2 // (m * (p2 - 1) + n2 - 1) - 1
    else:
        larger1 = k2 // (m * (p2 - 1) + n2 - 1)
    if less1 > larger1:
        return '-1 -1'
    if k1 == k2:
        return str(p2) + ' ' + str(n2)
    if k2 % (m * p2 - m + n2 - 1) == 0:
        larger = k2 // (m * p2 - m + n2 - 1) - 1
    else:
        larger = k2 // (m * p2 - m + n2 - 1)
    if k2 % (p2 * m - m + n2) == 0:
        smaller = k2 // (p2 * m - m + n2)
    else:
        smaller = k2 // (p2 * m - m + n2) + 1
    p1 = []
    n1 = []
    for a in range(smaller, larger + 1):
        if k1 % (a * m) == 0:
            p = k1 // (a * m)
        else:
            p = k1 // (a * m) + 1
        p1.append(p)
        if (k1 - (p - 1) * a * m) % a == 0:
            n1.append((k1 - (p - 1) * a * m) // a)
        else:
            n1.append((k1 - (p - 1) * a * m) // a + 1)
    if max(p1) > min(p1):
        ans1 = 0
    else:
        ans1 = p1[0]
    if max(n1) > min(n1):
        ans2 = 0
    else:
        ans2 = n1[0]

    return str(ans1) + ' ' + str(ans2)


n = list(map(int, input().split()))
print(find_P_and_N(n[0], n[1], n[2], n[3], n[4]))
