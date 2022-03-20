class Solution:
    def countPoints(self, rings: str) -> int:
        rc = {}
        i = 0
        while i < len(rings):
            if rings[i+1] in rc:
                rc[rings[i+1]].add(rings[i])
            else:
                rc[rings[i+1]] = {rings[i]}
            
            i += 2
        
        return len([1 for ring in rc.values() if len(ring) == 3])