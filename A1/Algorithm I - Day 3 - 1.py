class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        for i in range(len(nums)):
                if nums[i] == 0: 
                    count +=1
                elif not (count ==0):
                    aux = nums[i]
                    nums[i] = 0 
                    nums[i-count] = aux
