class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
                if nums[i] == 0: 
                    count +=1
                elif not (count ==0):
                    aux = nums[i]
                    nums[i] = 0 
                    nums[i-count] = aux