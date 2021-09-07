class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dct = {}
        for char in s:
            if char not in dct:
                dct[char] = 1
            else:
                dct[char] += 1
        
        return len(set(dct.values())) == 1