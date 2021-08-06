class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(n):
            cube = 3**i
            if cube == n:
                return True
            if cube > n:
                break
        return False