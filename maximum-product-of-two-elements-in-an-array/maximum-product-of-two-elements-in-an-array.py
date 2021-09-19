class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = -float('inf'), -float('inf')
        for num in nums:
            if num >= first:
                first, second = num, first
            elif second < num < first:
                second = num
            else:
                pass
        
        return (first-1)*(second-1)