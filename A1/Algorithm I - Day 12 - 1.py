class Solution:
    def climbStairs(self, n: int) -> int:
            count = 0
            n1, n2 = 0, 1
            
            while count < n:
                steps = n1 + n2
                n1 = n2
                n2 = steps
                count += 1
            return steps