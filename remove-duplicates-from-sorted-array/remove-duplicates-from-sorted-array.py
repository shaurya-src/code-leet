class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return nums[0]
        # [0,0,1,1,1,2,2,3,3,4]
        i = 1
        prev = nums[0]
        while i<len(nums):
            if prev == nums[i]:
                del nums[i]
            else:
                prev = nums[i]
                i += 1