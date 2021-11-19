class Solution:
    def reverseString(self, s):
        start = 0
        end = len(s) -1
        
        while (start<end): 
            aux = s[start]
            s[start] =s[end]
            s[end] = aux
            start +=1
            end -=1
