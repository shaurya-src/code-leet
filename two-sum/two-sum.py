class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        test = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if num in test:
                return [test[num], i]
            else:
                test[complement] = i
        return [-1, -1]