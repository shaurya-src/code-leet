class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = -float('inf')
        for i in range(len(nums)//2):
            res = max(res, nums[i] + nums[-1-i])
        return res