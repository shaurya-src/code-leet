class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for num in arr:
            if num not in occ:
                occ[num] = 1
            else:
                occ[num] += 1
        
        x = list(occ.values())
        return len(set(x)) == len(x)