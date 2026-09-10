class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        for i in range (len(s)):
            hm[s[i]]= hm.get(s[i],0)+1

        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i
        return -1