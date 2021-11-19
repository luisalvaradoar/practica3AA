import functools

class Solution:
    
    def recursing(self, val: int, setVals: set) -> bool:
        if val == 1:
            return True
        if val in setVals:
            return False
        setVals.add(val)
        digits = []
        while val >= 1:
            lst = val // 10
            digits.append(val - lst * 10)
            val = lst
        val = functools.reduce(lambda fst, snd: fst + snd, list(map(lambda val: val ** 2, digits)))
        return self.recursing(val, setVals)
    
    def isHappy(self, n: int) -> bool:
        return self.recursing(n, set())