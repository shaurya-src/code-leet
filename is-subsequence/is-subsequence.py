class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        i = 0
        while p<len(s) and i<len(t):
            if s[p] == t[i]:
                print("yo")
                p += 1
            i += 1
        return p == len(s)
