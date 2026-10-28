class Solution:
    def backvers(self,nums,start,end):
        while (start<end):
            nums[start],nums[end] = nums[end],nums[start]
            start +=1
            end-=1
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        length = len(nums)
        for i in range(length -2,-1,-1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        if idx == -1:
            self.backvers(nums,0,length-1)
            return
        self.backvers(nums,idx+1,length-1)
        new = -1
        for j in range(idx+1,length):
            if nums[idx] <nums[j]:
                new = j
                break
        nums[idx],nums[new] = nums[new],nums[idx]