class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1
        
        pair, left = 0, 0
        
        for key, value in dct.items():
            pair += value // 2
            left += value % 2
        
        return [pair, left]