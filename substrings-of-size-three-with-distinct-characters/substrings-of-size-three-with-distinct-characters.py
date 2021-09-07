class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        i = 0
        while i<len(s)-2:
            sub = s[i:i+3]
            oc = set()
            good = True
            for ch in sub:
                if ch in oc:
                    good = False
                    break
                else:
                    oc.add(ch)
            if good:
                count += 1
            i += 1
        return count