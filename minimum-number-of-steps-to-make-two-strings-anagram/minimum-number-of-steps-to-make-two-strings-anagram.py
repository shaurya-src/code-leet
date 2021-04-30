class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        for i in range(len(t)):
            if t[i] in s:
                s = s.replace(t[i], '', 1)
            else:
                count += 1
        
        return count