from collections import defaultdict

class Solution:
    def __init__(self):
        self.lut = defaultdict(int)
        for i in range(9):
            self.lut[str(i+1)] = 1
        
    def numDecodings(self, s: str) -> int:
        if s in self.lut.keys():
            return self.lut[s]
        
        cnt = 0
        if len(s) < 1 or s[0] == '0':
            self.lut[s] = cnt
            return cnt
        
        
        cnt += self.numDecodings(s[1:])
        
        if len(s) >= 2:
            if 1<= int(s[:2]) <= 26:
                if len(s) == 2:
                    cnt += 1
                else:                
                    cnt += self.numDecodings(s[2:])
        
        self.lut[s] = cnt
        return cnt    