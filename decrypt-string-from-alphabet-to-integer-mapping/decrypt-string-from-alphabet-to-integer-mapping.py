class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        res = ""
        while i >= 0:
            if s[i] == "#":
                idx = int(s[i-2:i])
                i -= 3  
            else:
                idx = int(s[i])
                i -= 1
            res += chr(idx + ord('a') - 1)
        return res[::-1]
            