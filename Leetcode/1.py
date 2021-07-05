class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i in range(len(nums)):
            if not target - nums[i] in h:
                h[nums[i]] = i
            else:
                return [i, h[target - nums[i]]]
