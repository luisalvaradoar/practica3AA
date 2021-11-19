class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        hash1 = dict()
        
        
        def sumcoin(amount):
            
            if amount ==0:
                return 0
            if amount <0:
                return float('inf')
            
            mini = float('inf')
            lent = len(coins)
            for i in range(0,lent):
                if amount-coins[i] in hash1.keys():
                    c = 1+hash1[amount-coins[i]]
                else:
                    c = 1 + sumcoin(amount-coins[i])
                if mini > c:
                    mini = c
            hash1[amount] = mini        
            return mini
        
        ans =  sumcoin(amount)
        
        
        if ans == float('inf'):
            return -1
        else:
            return ans