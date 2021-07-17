class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_num = sorted(nums)
        w, x, y, z = s_num[0], s_num[1], s_num[-1], s_num[-2]
        return (y*z) - (w*x)