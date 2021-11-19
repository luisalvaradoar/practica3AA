class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(index, curr): 
            if len(curr) > len(nums): 
                return 
            res.append(curr)
            for i in range(index, len(nums)): 
                recurse(i+1,curr+[nums[i]])
        recurse(0,[])
        return res