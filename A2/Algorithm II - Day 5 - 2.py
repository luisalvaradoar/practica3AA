class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, start, currProd = 0, 0, 1
        for end in range(len(nums)):
            currProd *= nums[end]
            while start <= end and currProd >= k:
                currProd //= nums[start]
                start += 1
            ans += (end - start) + 1
        return ans