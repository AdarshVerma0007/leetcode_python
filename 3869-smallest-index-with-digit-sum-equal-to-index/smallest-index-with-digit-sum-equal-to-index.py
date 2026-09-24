class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x = nums[i]
            Sum = 0
            while x>0:
                Sum += x%10
                x//=10
            if Sum == i:
                return i
        return -1
            