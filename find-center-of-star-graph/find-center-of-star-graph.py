class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dct = {}
        for e in edges:
            if e[0] not in dct:
                dct[e[0]] = [e[1]]
            else:
                # dct[e[0]].append(e[1])
                return e[0]
            
            if e[1] not in dct:
                dct[e[1]] = [e[0]]
            else:
                # dct[e[1]].append(e[0])
                return e[1]
        
        return -1 
            