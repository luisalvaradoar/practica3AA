class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            left = bisect.bisect_left(nums, target)
            right = bisect.bisect_right(nums, target)
            if left <= right - 1:
                return [left, right - 1]
            return [-1, -1]