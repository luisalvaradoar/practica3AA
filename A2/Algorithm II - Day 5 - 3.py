from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        min_len = inf
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum >= target:
                min_len = min(min_len, right-left+1)
                curr_sum -= nums[left]
                left += 1
        return min_len if min_len != inf else 0