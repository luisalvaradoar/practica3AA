class Solution:
    def reverseBits(self, n):
        res = 0
        for pos in range(32):
            bit = (n >> pos) & 1 
            res = (res << 1) + bit
        return res