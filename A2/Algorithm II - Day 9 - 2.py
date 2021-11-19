class Solution(object):
	def subsetsWithDup(self, nums):
		nums_len = len(nums)
		results = list()
		if nums_len == 0:  
			return results

		nums.sort()    
		from copy import deepcopy
		def get_next_index(nums, idx): 
			next_idx = idx
			while next_idx<nums_len and nums[next_idx]==nums[idx]: 
				next_idx += 1                
			return next_idx


		def back_track(nums, idx, subset, results): 
			if idx == nums_len:
				subset_copy = deepcopy(subset) 
				results.append(subset_copy)
			elif idx < nums_len: 
				back_track(nums, get_next_index(nums, idx), subset, results) 
				subset.append(nums[idx])
				back_track(nums, idx+1, subset, results) 
				subset.pop()
		subset = list()
		back_track(nums, 0, subset, results)    
		return results