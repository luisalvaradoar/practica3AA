class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, column = len(image), len(image[0])
        target = image[sr][sc]
        if target == newColor:
            return image
        def change(r,c):
            if r >= row or r < 0 or c >= column or c < 0:
                return None
            if image[r][c] != target:
                return None
            image[r][c] = newColor
            change(r+1,c)
            change(r-1,c)
            change(r,c+1)
            change(r,c-1)
            return None
        change(sr,sc)
        return image