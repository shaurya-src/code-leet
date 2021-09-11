class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # distribution -> p[0] always smallest, p[n-1], p[n] always largest
        # take count of # piles everyone will get -> len(piles)//3
        # iterate from back and take every second element
        
        piles.sort()
        limit = len(piles)//3
        res, i = 0, 1
        
        while limit > 0:
            res += piles[-1-i]
            i += 2
            limit -= 1
        
        return res