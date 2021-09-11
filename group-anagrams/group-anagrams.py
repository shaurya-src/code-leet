class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in dct:
                dct[key].append(word)
            else:
                dct[key] = [word]
        
        return list(dct.values())