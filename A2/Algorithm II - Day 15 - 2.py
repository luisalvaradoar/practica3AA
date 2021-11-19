class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        size = len(s)
        dp = [False]*(size+1)
        dp[size] = True 

        for i in range(size-1, -1, -1):
            for w in wordDict:
                w_size = len(w)
                if s[i:i+w_size] == w:
                    dp[i] = dp[i + w_size] 
                    if dp[i]:
                        break 
        return dp[0]