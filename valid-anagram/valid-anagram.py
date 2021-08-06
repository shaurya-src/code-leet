class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(string):
            dct = {}
            for letter in string:
                if letter not in dct:
                    dct[letter] = 1
                else:
                    dct[letter] += 1
            return dct
        
        sc = count(s)
        tc = count(t)
        
        if sc == tc:
            return True
        
        return False