def ifSimilar(num1, num2):
    ind1 = len(num1) - 1
    ind2 = len(num2) - 1
    num = 0
    while ind1 > -1 and ind2 > -1:
        while a[ind1] == "-" or a[ind1] == "(" or a[ind1] == ")":
            ind1 -= 1
        while b[ind2] == "-" or b[ind2] == "(" or b[ind2] == ")":
            ind2 -= 1
        if ind1 > -1 and ind2 > -1:
            num += 1
            if num == 11:
                return 'YES'
            if a[ind1] != b[ind2]:
                return 'NO'
        ind1 -= 1
        ind2 -= 1
    if ind1 == ind2:
        return 'YES'
    if ind1 == -1:
        while num != 10:
            while b[ind2] == "-" or b[ind2] == "(" or b[ind2] == ")":
                ind2 -= 1
            num += 1
            if num == 8:
                if b[ind2] != '5':
                    return 'NO'
            if num == 9:
                if b[ind2] != '9':
                    return 'NO'
            if num == 10:
                if b[ind2] != '4':
                    return 'NO'
            ind2 -= 1
        return 'YES'
    if ind2 == -1:
        while num != 10:
            while a[ind1] == "-" or a[ind1] == "(" or a[ind1] == ")":
                ind1 -= 1
            num += 1
            if num == 8:
                if a[ind1] != '5':
                    return 'NO'
            if num == 9:
                if a[ind1] != '9':
                    return 'NO'
            if num == 10:
                if a[ind1] != '4':
                    return 'NO'
            ind1 -= 1
        return 'YES'


a = input()
for i in range(3):
    b = input()
    print(ifSimilar(a, b))
