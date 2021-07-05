class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last_let = chars[0]
        last_count = 0
        index = 0
        for x in chars:
            if x == last_let:
                last_count += 1
            else:
                chars[index] = last_let
                index += 1
                if last_count > 1:
                    for i in range(len(str(last_count))):
                        chars[index] = str(last_count)[i]
                        index += 1
                last_let = x
                last_count = 1
        chars[index] = x
        index += 1
        if last_count > 1:
            for i in range(len(str(last_count))):
                chars[index] = str(last_count)[i]
                index += 1
        del chars[index:]
        return len(chars)


ch=['1','3','5','7']
ch[0:3]='2'
print(ch)
