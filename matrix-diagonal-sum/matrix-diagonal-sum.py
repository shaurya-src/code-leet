class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row=len(mat)
        res=0
        k=len(mat[0])-1
        for i in range(row):
            res+=mat[i][i]
            res+=mat[i][k] if k!=i else 0
            k-=1
        return res