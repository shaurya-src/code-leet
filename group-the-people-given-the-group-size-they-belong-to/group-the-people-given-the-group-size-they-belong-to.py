class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # size -> index
        dct = {}
        res = []
        
        for idx, size in enumerate(groupSizes):
            if size not in dct:
                dct[size] = [idx]
            else:
                dct[size].append(idx)
        
        for size, idx in dct.items():
            while len(idx) != 0:
                res.append(idx[:size])
                del idx[:size]
        return res