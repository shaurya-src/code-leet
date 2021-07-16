class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        occur = {}
        for num in nums:
            if num not in occur:
                occur[num] = True
            else:
                return occur[num]
        return False