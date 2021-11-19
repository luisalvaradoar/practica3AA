import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cnums = nums[:]        

    def reset(self) -> List[int]:
        self.cnums = self.nums[:]
        return self.cnums

    def shuffle(self) -> List[int]:
        newnums = []
        
        while self.cnums:
            newnums.append(self.cnums.pop(random.randint(0, len(self.cnums)-1)))
        
        self.cnums = newnums
        return self.cnums