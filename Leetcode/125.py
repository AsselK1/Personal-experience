class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start].upper() != s[end].upper():
                    return False
                else:
                    start += 1
                    end -= 1
                continue
            if not s[start].isalnum():
                start += 1
            if not s[end].isalnum():
                end -= 1
        return True


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1;
            r -= 1
        return True
