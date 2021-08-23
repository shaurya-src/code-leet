class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force
        ar = nums1 + nums2
        ar.sort()
        n = len(ar)
        
        median = ar[n//2]
        
        if n%2 != 0:
            return median
        else:
            return (median + ar[(n//2)-1])/2