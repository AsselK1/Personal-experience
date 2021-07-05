numbers = list(map(int, input().split()))
max_1_pos = None
max_2_pos = None
max_1_neg = None
max_2_neg = None
for i in range(len(numbers)):
    if numbers[i] >= 0:
        if max_1_pos is None:
            max_1_pos = numbers[i]
        elif max_2_pos is None:
            if numbers[i] >= max_1_pos:
                max_2_pos = max_1_pos
                max_1_pos = numbers[i]
            else:
                max_2_pos = numbers[i]
        else:
            if numbers[i] >= max_1_pos:
                max_2_pos = max_1_pos
                max_1_pos = numbers[i]
            elif numbers[i] >= max_2_pos:
                max_2_pos = numbers[i]
    else:
        if max_1_neg is None:
            max_1_neg = numbers[i]
        elif max_2_neg is None:
            if numbers[i] <= max_1_neg:
                max_2_neg = max_1_neg
                max_1_neg = numbers[i]
            else:
                max_2_neg = numbers[i]
        else:
            if numbers[i] <= max_1_neg:
                max_2_neg = max_1_neg
                max_1_neg = numbers[i]
            elif numbers[i] <= max_2_neg:
                max_2_neg = numbers[i]
if max_1_pos is not None and max_2_pos is not None and max_1_neg is not None and max_2_neg is not None:
    if max_2_pos == 0:
        print(max_1_neg, max_2_neg)
    elif -max_1_pos / max_1_neg > -max_2_neg / max_2_pos:
        print(max_2_pos, max_1_pos)
    else:
        print(max_1_neg, max_2_neg)
elif max_1_pos is not None and max_2_pos is not None:
    print(max_2_pos, max_1_pos)
elif max_2_neg is not None and max_1_neg is not None:
    print(max_1_neg, max_2_neg)
else:
    print(max_1_neg, max_1_pos)
