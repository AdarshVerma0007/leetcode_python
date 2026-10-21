class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        Set ={}
        for i in range (len(nums)):
            if nums[i] in Set and abs(i-Set[nums[i]]) <=k:
                return True
            Set[nums[i]] = i
        return False