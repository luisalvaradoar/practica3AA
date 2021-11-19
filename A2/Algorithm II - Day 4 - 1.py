class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        tmp1 = []
        tmp2 = []
        
        for c in s: 
            if c != '#':
                tmp1.append(c) 
            else:
                if len(tmp1) > 0 : 
                    tmp1.pop() 
        
        tmp1 = "".join(tmp1) 
        
        
        for c in t: 
            if c != '#':
                tmp2.append(c) 
            else:
                if len(tmp2) > 0 : 
                    tmp2.pop() 
        
        tmp2 = "".join(tmp2) 
        
        return tmp1 == tmp2 