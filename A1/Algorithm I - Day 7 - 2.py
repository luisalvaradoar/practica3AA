class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		self.grid = grid 
		max_ = 0
		for row in range(len(grid)):
			for column in range(len(grid[0])):
				if grid[row][column] == 1:
					self.count = 1
					sets = set()
					sets.add((row, column))
					self.travel(row, column, sets)
					max_ = max(max_,self.count)
		return max_

	def travel(self, row, column, seen):
		if row-1 >=0 and (row-1, column) not in seen and self.grid[row-1][column] == 1:
			self.count += 1
			self.grid[row-1][column] = 0
			seen.add((row-1,column))
			self.travel(row-1, column, seen)
		if row+1 < len(self.grid) and (row+1, column) not in seen and self.grid[row+1][column] == 1:
			self.count += 1
			self.grid[row+1][column] = 0
			seen.add((row+1,column))
			self.travel(row+1, column, seen)
		if column+1 < len(self.grid[0]) and (row, column+1) not in seen and self.grid[row][column+1] == 1:
			self.count += 1
			self.grid[row][column+1] = 0
			seen.add((row,column+1))
			self.travel(row, column+1, seen)
		if column-1 >= 0 and (row, column-1) not in seen and self.grid[row][column-1] == 1:
			self.count += 1
			self.grid[row][column-1] = 0
			seen.add((row,column-1))
			self.travel(row, column-1, seen)