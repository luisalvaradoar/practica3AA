class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return []
        if len(nums) < 3:
            return []
        n=len(nums)
        i = 0
        res = []
        nums.sort()
        while i < n-2 and nums[i] <= 0:
            l = i+1
            r = n-1
            while l<r:                      
                currSum = nums[i] + nums[l] + nums[r]
                
                if currSum > 0:
                    r -= 1
  
                elif currSum < 0:
                    l += 1
                    
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    l += 1
                    r -= 1
            while i < n-2 and nums[i] == nums[i+1]:
                i += 1            
            i += 1
            
        return res