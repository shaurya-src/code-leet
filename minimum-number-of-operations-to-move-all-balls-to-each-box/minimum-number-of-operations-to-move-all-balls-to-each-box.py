class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        lr = 0
        for i in range(len(boxes)):
            lr = sum([abs(i-x) for x in range(len(boxes)) if boxes[x] == '1'])
            result.append(lr)
        return result