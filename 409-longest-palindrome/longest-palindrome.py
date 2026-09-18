class Solution:
    def longestPalindrome(self, s: str) -> int:
        f={}
        res = 0
        for i in range (len(s)):
            f[s[i]] = f.get(s[i],0)+1
        odd = False
        for char ,val in f.items():
            if val%2 ==0:
                res +=val
            else:
                odd = True
        if odd == False:
            return res
        else:
            for char,val in f.items():
                if val %2 ==1:
                    res+=val -1
        return res+1
