class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have = {}
        for i in range (len(text)):
            have[text[i]]= have.get(text[i],0)+1
        need = {}
        need['b']= 1
        need['a']= 1
        need['l']= 2
        need['o']= 2
        need['n']= 1
        res = float(inf)
        for char,f_need in need.items():
            f_have = have.get(char,0)
            times = f_have//f_need
            res = min(res,times)
        return res
