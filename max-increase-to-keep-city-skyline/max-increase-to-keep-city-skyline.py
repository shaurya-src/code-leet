class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = [max(x) for x in grid]
        col_max = []
        for i in range(len(grid)):
            cm = 0
            for j in range(len(grid)):
                cm = max(cm, grid[j][i])
            col_max.append(cm)
        
        extra = 0
        
        for i in range(len(grid)):
            for j in range(len(grid)):
                limit = min(row_max[i], col_max[j])
                extra += limit - grid[i][j]
        # print(row_max)
        # print(col_max)
        return extra