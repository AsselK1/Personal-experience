def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    end = 1  # inclusive
    start = 0
    d = {s[start]: 1}
    change = 0
    max_ = s[start]
    len_max = 1
    len_coor=[s[0], s[0]]
    while end < len(s):
        if s[end] != max_:
            d[s[end]] = d.get(s[end], 0) + 1
            if d[s[end]] > d[max_]:
                max_ = s[end]
            else:
                change += 1
        else:
            d[max_] += 1
        while change > k:
            if s[start] != max_:
                change -= 1
                start += 1
            else:
                start += 1
                d[max_] -= 1
                if max(d.values()) > d[max_]:
                    change -= 1
                    max_ = max(d, key=d.get)
        if end-start+1 > len_max:
            len_coor=[s[start], s[end]]
        len_max = max(len_max, end-start+1)
        end += 1
    return len_coor


print(characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))
