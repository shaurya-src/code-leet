class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cm = max(candies)
        
        return [True if x+extraCandies>=cm else False for x in candies]
        