from collections import defaultdict
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        d = defaultdict(int)
        for x in candidates:
            d[x] += 1
        candidates = sorted(list(set(candidates)))
        dp = [[[[]] if i == 0 else [] for i in range(target+1)] for _ in range(len(candidates)+1)]
        for i in range(len(candidates)-1, -1, -1):
            x = candidates[i]
            for j in range(x, target+1):
                for k in range(min(j//x, d[x])+1):
                    dp[i][j].extend([[x]*k+l for l in dp[i+1][j-x*k]])
        return dp[0][target]