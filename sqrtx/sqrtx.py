class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        res = -1
        
        for i in range(x):
            if i*i > x:
                break    
            res = i
        
        return res