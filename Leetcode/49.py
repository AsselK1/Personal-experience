class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        ans = []
        for i in range(len(strs)):
            a = ''.join(sorted(strs[i]))
            if a in d:
                d[a].append(i)
            else:
                d[a] = [i]
        x = []
        for key in d:
            for ind in d[key]:
                x.append(strs[ind])
            ans.append(x)
            x = []
        return ans


# REVIEW!
class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return d.values()
