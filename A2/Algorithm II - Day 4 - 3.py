class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        def calc_area(l, r):
            w = r -l
            h = min(height[r], height[l]) 
            return w*h
        
        hMax = max(height)
        
        l, r = 0, len(height) - 1       
        maxArea = 0
        while l<r:
            maxArea = max(calc_area(l, r), maxArea)
            if (r-l) * hMax < maxArea:
                break
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea