class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        Sum = 0
        f = {0:1}
        for i in range (len(nums)):
            Sum+= nums[i]
            rem = Sum% k
            if rem<0:
                rem += k
            res += f.get(rem,0)
            f[rem] = f.get(rem,0)+1
        return res 
