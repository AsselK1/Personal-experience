class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='':
            return 0
        if len(s)==1:
            return 1
        start=0
        end=1
        longest=1
        while end<len(s):
            while s[start]!=s[end] and end<len(s):
                end+=1
            longest=max(longest, end-start+1)
            start+=1
        return longest
