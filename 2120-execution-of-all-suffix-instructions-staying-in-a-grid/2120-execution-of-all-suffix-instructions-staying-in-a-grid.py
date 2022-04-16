class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        for i in range(len(s)):
            inst = s[i:]
            row, col = startPos
            curr_dist = 0
            for move in inst:
                if move == 'U':
                    row -= 1
                elif move == 'D':
                    row += 1
                elif move == 'L':
                    col -= 1
                elif move == 'R':
                    col += 1
                if 0 <= row < n and 0 <= col < n:
                    curr_dist += 1
                else:
                    break
            result.append(curr_dist)
        return result