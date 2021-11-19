class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = 1
        sum_val = m + n - 2
        for i in range(0, m - 1):
            answer = answer * (sum_val - i) // (i + 1)
        return answer