class Solution(object):
	def minDistance(self, word1, word2):
		if word1 == word2:
			return 0
		word1_len, word2_len = len(word1), len(word2) 

		if word1_len<word2_len: 
			word1_len, word2_len = word2_len, word1_len
			word1, word2 = word2, word1        

		dp = [j for j in range(word2_len+1)]        

		for i in range(1, word1_len+1): 
			prev = dp[0]
			for j in range(1, word2_len+1):
				temp = dp[j]
				if word1[i-1] == word2[j-1]:
					dp[j] = prev

				else:
					dp[j] = min(dp[j]+1, prev+1, dp[j-1]+1)
				prev = temp
			dp[0] = i    

		return dp[word2_len] 