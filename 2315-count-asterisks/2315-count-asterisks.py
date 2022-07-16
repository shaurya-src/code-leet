class Solution:
    def countAsterisks(self, s: str) -> int:
        opn = False
        count = 0
        for ch in s:
            if ch == '|':
                opn = not opn
                continue
            
            if not opn and ch == '*':
                count += 1
                
        return count