class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        cur = 0
        i = 0
        if seats[i] == 0:
            while seats[i] != 1:
                cur += 1
                i += 1
            ans = max(ans, cur)
            cur = 0
        j = len(seats) - 1
        if seats[j] == 0:
            while seats[j] != 1:
                cur += 1
                j -= 1
            ans = max(ans, cur)
            cur = 0
        k = i
        while k <= j:
            while k <= j and seats[k] == 0:
                cur += 1
                k += 1
            k += 1
            ans = max(ans, (cur + 1) // 2)
            cur = 0
        return ans
