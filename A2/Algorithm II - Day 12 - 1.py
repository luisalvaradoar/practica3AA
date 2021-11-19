class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo=dict()
        def rob_linear(nums,l,r): #returns the linear max rob of nums[l:r]
            if r<=l: return 0
            
            if (l,r) in memo: return memo[l,r]
            
            rob_left=nums[l]+rob_linear(nums,l+2,r)
            no_rob_left=rob_linear(nums,l+1,r)
            
            memo[l,r]=max(rob_left, no_rob_left)
            
            return memo[l,r]
        
        N=len(nums)
        
        first_rob=nums[0]+rob_linear(nums,2,N-1)
        no_first_rob=rob_linear(nums,1,N)
        return max(first_rob,no_first_rob)