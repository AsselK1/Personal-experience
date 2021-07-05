def aircon():
    n = int(input())
    classes = list(map(int, input().split()))
    m = int(input())
    hm = {}
    a = set()
    for _ in range(m):
        x = list(map(int, input().split()))
        if x[0] in a:
            if x[1] < hm[x[0]][-1]:
                hm[x[0]].append(x[1])
        else:
            a.add(x[0])
            hm[x[0]] = [x[1]]
    b = []
    for k in a:
        b.append(k)
    b.sort()
    classes.sort(reverse=True)
    mediums = []
    start = len(b) - 1
    end = -1
    total = 0
    for i in range(len(classes)):
        if len(mediums) < 1 or mediums[-1][1] != classes[i]:
            price = float('inf')
            for j in range(start, end, -1):
                if b[j] > classes[i]:
                    if hm[b[j]][-1] < price:
                        price = hm[b[j]][-1]
                elif b[j] == classes[i]:
                    if hm[b[j]][-1] < price:
                        price = hm[b[j]][-1]
                    break
                else:
                    break
            if len(mediums) > 1 and mediums[-1][0] < price:
                price = mediums[-1][0]
            mediums.append([price, classes[i]])
            start = j
            total += price
        else:
            total += mediums[-1][0]
    return total


print(aircon())
