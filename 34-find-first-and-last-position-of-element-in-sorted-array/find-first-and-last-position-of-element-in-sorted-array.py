class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return[self.bin(nums,target,True),self.bin(nums,target,False)]
    def bin(self,nums,target,first):
        n = len(nums)
        low = 0
        high = n-1
        res=-1
        while(low <= high):
            guess= (low+high)//2
            if nums[guess]<target:
                low = guess+1
            elif nums[guess]> target:
                high = guess-1
            else:
                res = guess
                if first:
                    high = guess-1
                else:
                    low= guess+1
        return res