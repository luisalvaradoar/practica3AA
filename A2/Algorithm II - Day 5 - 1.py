class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        ref_map = Counter(p)
        win_map = Counter(s[:len(p)-1])
        
        
        res = []
        
        for left in range(len(s)-len(p)+1):
            right = left + len(p) - 1
            win_map[s[right]] += 1
            if win_map == ref_map:
                res.append(left)
            win_map[s[left]] -= 1
            if win_map[s[left]] == 0: del win_map[s[left]]
            left += 1
        
        return res