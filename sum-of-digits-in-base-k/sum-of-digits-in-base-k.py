class Solution:
    def sumBase(self, n: int, k: int) -> int:
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n%k))
            n //= k
            
        return sum(digits)