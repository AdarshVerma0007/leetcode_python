class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0:-1}
        zero = 0
        one = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zero +=1
            else:
                one +=1
            diff = zero - one
            if diff == 0:
                ans = max(ans,i+1)
                continue
            if diff not in mp:
                mp[diff] = i
            else:
                idx = mp[diff]
                Len = i - idx
                ans = max(Len,ans)
        return ans
