class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hdict = {}
        us = 0
        for i in nums:
            if i not in hdict:
                hdict[i] = 1
            else:
                hdict[i] += 1
        
        for key, value in hdict.items():
            if value == 1:
                us += key
        return us