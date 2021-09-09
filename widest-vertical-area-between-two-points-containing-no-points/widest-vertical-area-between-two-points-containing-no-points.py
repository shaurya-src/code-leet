class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = sorted(set([x[0] for x in points]))
        max_diff = 0
        for i in range(1, len(arr)):
            curr = arr[i] - arr[i-1]
            max_diff = max(max_diff, curr)
        return max_diff