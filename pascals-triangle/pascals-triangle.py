class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return result
        else:
            for i in range(2, numRows):
                row = [1]*(i+1)
                for x in range(1, len(row)-1):
                    row[x] = result[i-1][x-1] + result[i-1][x]
                result.append(row)
            return result
        