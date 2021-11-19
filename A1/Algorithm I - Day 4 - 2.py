class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        for i in range(len(a)):
            temp=a[i]
            a[i]=temp[::-1]
        s = ' '.join(a)
        return s