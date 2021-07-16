class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_global = -float('inf')
        max_current = 0
        
        for i in range(len(nums)):
            max_current += nums[i]
            max_global = max(max_current, max_global)
            
            if max_current < 0:
                max_current = 0
        return max_global