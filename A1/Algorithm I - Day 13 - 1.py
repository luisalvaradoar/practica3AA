class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: 
            return False
        if n == 1:
            return True

        while True:
            if n % 2 != 0:
                return False
            elif n == 2:
                return True
            n /= 2