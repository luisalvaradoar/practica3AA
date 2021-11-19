from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
        res = [[]]
        def add_key_single(key, num, l):
            if num == 0:
                return [l]
            if not l:
                return [[key] * num]
            else:
                ls = []
                for i in range(num+1):
                    prefix = [key] * (num-i) + [l[0]]
                    for perm in add_key_single(key, i, l[1:]):
                        ls.append(prefix + perm)
                return ls
            
        for key in d:
            new_res = []
            for l in res:
                for perm in add_key_single(key, d[key], l):
                    new_res.append(perm)
            res = new_res
        return res