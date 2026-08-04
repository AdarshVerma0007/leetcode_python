class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0 
        Sum = sum(nums)
        for i in range(len(nums)):
            right = Sum - nums[i] - left
            if(left ==right):
                return i
            left += nums[i]
            
        return -1