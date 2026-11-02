class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        min_pre =0
        count = 0
        for num in nums:
            count += num
            min_pre = min(min_pre,count)
        return 1-min_pre