numbers = []
while True:
    number = int(input())
    if number == -2000000000:
        break
    numbers.append(number)


def what_mode(arr):
    if len(arr) == 1:
        return "CONSTANT"

    if arr[0] == arr[1]:
        mode = "CONSTANT"

    if arr[0] < arr[1]:
        mode = "ASCENDING"

    if arr[0] > arr[1]:
        mode = "DESCENDING"

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            if mode == "ASCENDING":
                mode = "WEAKLY ASCENDING"
            elif mode == "DESCENDING":
                mode = "WEAKLY DESCENDING"
        if arr[i] < arr[i + 1]:
            if mode == "CONSTANT":
                mode = "WEAKLY ASCENDING"
            if mode == "DESCENDING" or mode == "WEAKLY DESCENDING":
                mode = "RANDOM"
        if arr[i] > arr[i + 1]:
            if mode == "CONSTANT":
                mode = "WEAKLY DESCENDING"
            if mode == "ASCENDING" or mode == "WEAKLY ASCENDING":
                mode = "RANDOM"
    return mode


print(what_mode(numbers))
