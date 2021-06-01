class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i, num in enumerate(arr):
            if num in target:
                target.remove(num)
            else:
                return False
        
        return True