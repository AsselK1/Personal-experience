class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        if len(nums) == 0:
            return
        start = nums[0]
        end = nums[0]
        for i in range(len(nums) - 1):
            if 1 == nums[i + 1] - nums[i]:
                end += 1
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(end))
                start = nums[i + 1]
                end = nums[i + 1]
        if start == end:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(end))
        return ans
