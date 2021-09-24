class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = self.recurGrid(m, n)
        return result
    
    def recurGrid(self, m, n, memo = {}):
        key1, key2 = str(m) + ',' + str(n), str(n) + ',' + str(m)
        if m == n == 1:
            return 1
        
        if m == 0 or n == 0:
            return 0
        
        if key1 in memo:
            return memo[key1]
        else:
            memo[key1] = self.recurGrid(m-1, n, memo) + self.recurGrid(m, n-1, memo)
            memo[key2] = memo[key1]
            return memo[key1]