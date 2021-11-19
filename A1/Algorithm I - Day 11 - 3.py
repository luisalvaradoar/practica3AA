class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        op=[]
        def form(i,s,p):
            if i==S:
                op.append(p)
                return
            if s[i].isdigit():
                form(i+1,s,p+s[i])
            else:
                form(i+1,s,p+s[i].lower())
                form(i+1,s,p+s[i].upper())

        S=len(s)
        form(0,s,"")
        return op