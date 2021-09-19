class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = list(range(1, (n//2)+1))
        arr += list(range(-(n//2), 0))
        
        if n%2 != 0:
            arr.append(0)
        
        return arr