class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            middle = (low + high) // 2
            if target == nums[middle]:
                return middle
            if target > nums[middle]:
                low = middle + 1
            else:
                high = middle
        return low