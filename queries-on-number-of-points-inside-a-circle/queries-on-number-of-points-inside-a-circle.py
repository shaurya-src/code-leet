from math import sqrt
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for circle in queries:
            pt1 = circle[:2]
            rad = circle[-1]
            count = 0
            for pt in points:
                dist = self.get_distance(pt1, pt)
                if dist<= rad:
                    count += 1
            res.append(count)        
        
        return res
    
    def get_distance(self, pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2
        
        dist = sqrt((x2-x1)**2 + (y2-y1)**2)
        
        return dist