class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        return len([1 for x in stones if x in jewels])