class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def helper(arr):
            left, right = 0, len(arr)
            mid = left + (right-left)//2
            
            if arr[mid-1] < arr[left]:
                arr = arr[:mid]
            elif arr[mid] > arr[right-1]:
                arr = arr[mid:]
            else:
                return min(arr[left], arr[mid])
            
            return helper(arr)
                
        return helper(nums)