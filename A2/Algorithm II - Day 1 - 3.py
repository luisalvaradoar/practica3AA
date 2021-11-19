class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        low = 0
        high = n-1
        
        while low>=0 and low<m and high>=0 and high<n:
            if matrix[low][high] == target:
                return True
            elif matrix[low][high] < target:
                low = low + 1
            elif matrix[low][high] > target:
                high = high - 1
        return False