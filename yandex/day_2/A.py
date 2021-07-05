a = list(map(int, input().split()))


def isAscending(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return "NO"
    return "YES"


print(isAscending(a))
