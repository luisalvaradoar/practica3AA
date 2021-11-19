class Solution(object):
    def lengthOfLongestSubstring(self, s):
        visited = defaultdict(int)
        maxLen = 0
        i = 0
        for j,char in enumerate(s):
            if char in visited:
                i = max(i, visited[char]+1)
            visited[char] = j
            maxLen =  max(maxLen, j-i+1)

        return maxLen