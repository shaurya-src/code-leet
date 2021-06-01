class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        cm = 0
        for dim in rectangles:
            if min(dim) > cm:
                cm = min(dim)
        
        return len([1 for rect in rectangles if min(rect)==cm])