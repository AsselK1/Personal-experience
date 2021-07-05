a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())


def lin_sol(a, b, c, d, e, f):
    if a * d - b * c != 0:
        y = (a * f - c * e) / (a * d - b * c)
        x = (d * e - b * f) / (a * d - b * c)
        return str(2) + ' ' + str(x) + ' ' + str(y)
    else:
        if a == 0 and b == 0 and e != 0:
            return str(0)
        if c == 0 and d == 0 and f != 0:
            return str(0)
        if a * f - c * e != 0 or d * e - b * f != 0:
            return str(0)
        if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
            return str(5)
        if a == 0 and c == 0 and b == 0:
            return str(4) + ' ' + str(f / d)
        elif a == 0 and c == 0:
            return str(4) + ' ' + str(e / b)
        if b == 0 and d == 0 and a == 0:
            return str(3) + ' ' + str(f / c)
        elif b == 0 and d == 0:
            return str(3) + ' ' + str(e / a)
        if a == 0:
            return str(1) + ' ' + str(-c / d) + ' ' + str(f / d)

        return str(1) + ' ' + str(-a / b) + ' ' + str(e / b)


print(lin_sol(a, b, c, d, e, f))
