class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = {}
        have = {}
        for i in range (len(ransomNote)):
            need[ransomNote[i]] = need.get(ransomNote[i],0)+1
        for j in range (len(magazine)):
            have[magazine[j]] = have.get(magazine[j],0)+1
        return self.fun(have,need)
    def fun(self,have, need) ->bool:
        for char, count in need.items():
            if have.get(char,0) < count:
                return False
        return True

