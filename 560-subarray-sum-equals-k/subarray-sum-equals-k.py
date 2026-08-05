class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Sum = 0 
        res = 0
        hashmap = {0:1}
        for num in nums:
            Sum+=num
            res += hashmap.get(Sum-k,0)
            hashmap[Sum] = hashmap.get(Sum,0)+1
        return res
