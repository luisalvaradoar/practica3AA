class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        bottom_zeros = [0 for row in range(len(triangle) + 1)]
        triangle.append(bottom_zeros)
        
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                triangle[row][i] = min(triangle[row][i] + triangle[row + 1][i],
                                       triangle[row][i] + triangle[row + 1][i + 1])
                
        return triangle[row][i]