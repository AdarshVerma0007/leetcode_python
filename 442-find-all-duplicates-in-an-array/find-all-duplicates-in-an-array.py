class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        ans = []
        for x in nums:
            index = abs(x) - 1
            if nums[index] <0:
                ans.append(abs(x))
            else:
                nums[index] = -nums[index]
        return ans