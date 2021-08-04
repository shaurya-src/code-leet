class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct = {}
        for i, letter in enumerate(s):
            if letter not in dct:
                dct[letter] = [i, 1]
            else:
                dct[letter][-1] += 1
        
        for key, value in dct.items():
            index = value[0]
            count = value[-1]
            if count == 1:
                return index
        
        return -1