class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lc = 0
        rc = 0
        count = 0
        for ch in s:
            if ch == 'L':
                lc += 1
            else:
                rc += 1
            
            if lc == rc:
                count += 1
        return count