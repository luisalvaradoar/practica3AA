class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        jump_count = [0] * N
		
        for i in range(N):
            if i == 0:
                jump_count[0] = 1
    
            if jump_count[i] == 0:
                continue
            
            for j in range(1, nums[i] + 1):
                if i + j >= N:
                    continue
                jump_count[i + j] = 1
                if i + j == N - 1:
                    return True
                
        return True if jump_count[N - 1] == 1 else False