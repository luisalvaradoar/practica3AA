class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        
        if n == 1:
            return 0
        
        for i in range(1, n):
            if i == n-1 and nums[i] > nums[i-1]:
                res = i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                res = i
                
        return res