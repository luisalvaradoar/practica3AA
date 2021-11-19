class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		res = []
		sol = []
		root = nums
		def DFS(root, sol):
			if not root:
				res.append(sol[:].copy())
				return
			for i in range(len(root)):
				sol.append(root[i])
				if i == len(root):
					DFS(root[:i], sol)
				else:
					DFS(root[:i]+root[i+1:], sol)
				sol.pop()

		DFS(root, sol=[])
		return res