class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ns = sorted(nums)
        return [ns.index(i) for i in nums]