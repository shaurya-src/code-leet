class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        a = 1
        b = 2
        res = -1
        
        for i in range(3, n+1):
            res = a + b
            a = b
            b = res
        
        return res