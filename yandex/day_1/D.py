def findSol(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return 'MANY SOLUTIONS'
            else:
                return 'NO SOLUTION'
        if c > 0 and b == c ** 2:
            return 'MANY SOLUTIONS'
        else:
            return 'NO SOLUTION'
    if c < 0:
        return 'NO SOLUTION'
    else:
        if (c ** 2 - b) % a == 0:
            return (c ** 2 - b) // a
        return 'NO SOLUTION'


a = int(input())
b = int(input())
c = int(input())
print(findSol(a, b, c))
