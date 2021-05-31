class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def getVal(num):
            return sum(list(map(int, list(str(num)))))
        
        boxes = {}
        
        for i in range(lowLimit, highLimit+1):
            x = getVal(i)
            if x not in boxes:
                boxes[x] = 1
            else:
                boxes[x] += 1
            
        return max(list(boxes.values()))
                