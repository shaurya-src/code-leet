class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = sorted(heights)
        return len([1 for i, height in enumerate(heights) if height != exp[i]])