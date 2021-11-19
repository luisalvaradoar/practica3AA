class Solution:
    def bsearch(self,nums,left,right,target)->int:
        if right<left:
            return -1
        mid=(right+left)//2
        if nums[mid]==target:
            return mid
        elif target>nums[mid]:
            return self.bsearch(nums,mid+1,right,target)
        else:
            return self.bsearch(nums,left,mid-1,target)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        return self.bsearch(nums,0,len(nums)-1,target)