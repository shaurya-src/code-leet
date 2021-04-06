class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        cp = digits[0]
        for i in range(1, len(digits)):
            cp *= digits[i]
            
        return cp - sum(digits)