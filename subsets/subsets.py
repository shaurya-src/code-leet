from itertools import combinations as comb
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            curr = comb(nums, i)
            res.extend(curr)
        return res