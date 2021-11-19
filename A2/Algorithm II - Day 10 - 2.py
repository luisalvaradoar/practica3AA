class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i,sublist,res):
            if sum(sublist) == target:
                res.append(sublist.copy())
            for j in range(i,len(candidates)):
                newlist = sublist + [candidates[j]]
                if sum(newlist)<= target:
                    dfs(j,newlist,res)
            return None
                
                
                
        res = []
        for i in range(0,len(candidates)):
            if i <= target:
                dfs(i,[candidates[i]],res)
        return res