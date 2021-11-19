class Solution:
    def integerBreak(self, n: int) -> int:

        out=1

        if n==2:
            return 1

        if n==3:
            return 2

        q=n
        while q>4:
            q=q-3
            out*=3

        if q!=0:
            out*=q
        return out