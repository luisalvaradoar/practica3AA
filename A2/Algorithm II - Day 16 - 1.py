class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
        return max(dp)