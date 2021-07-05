class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        cur_sum = 0
        count = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            count += sums.get(cur_sum - k, 0)
            sums[cur_sum] = sums.get(cur_sum, 0) + 1
        return count
