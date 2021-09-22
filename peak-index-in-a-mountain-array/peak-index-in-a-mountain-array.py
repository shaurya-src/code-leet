class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # value, idx
        peak_idx = [-float('inf'), -1]
        for i, num in enumerate(arr):
            if num > peak_idx[0]:
                peak_idx = [num, i]
        
        return peak_idx[-1]