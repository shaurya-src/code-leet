class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cm = nums[0]
        i = 1
        ops = 0
        while i < len(nums):
            if nums[i] > cm:
                cm = nums[i]
                i += 1
                
            else:
                cm += 1
                ops += cm - nums[i]
                i += 1
        return ops