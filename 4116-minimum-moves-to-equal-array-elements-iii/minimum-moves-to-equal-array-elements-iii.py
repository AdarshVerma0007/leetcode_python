class Solution:
    def minMoves(self, nums: List[int]) -> int:
        Max = max(nums)
        res = 0
        for x in nums:
            res += Max-x
        return res