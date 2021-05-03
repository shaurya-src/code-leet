class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            neg = len([-1 for x in nums if x<0])
            if (neg%2 != 0):
                return -1
            else:
                return 1