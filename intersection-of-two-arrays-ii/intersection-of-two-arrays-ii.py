class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = {}
        c2 = {}
        
        for i in range(len(nums1)):
            if nums1[i] not in c1:
                c1[nums1[i]] = 1
            else:
                c1[nums1[i]] += 1
        
        for i in range(len(nums2)):
            if nums2[i] not in c2:
                c2[nums2[i]] = 1
            else:
                c2[nums2[i]] += 1
        
        result = []
        
        keys = set(list(c1.keys()) + list(c2.keys()))
        
        for key in keys:
            if key in c1 and key in c2:
                v1, v2 = c1[key], c2[key]
                count = min(v1, v2)
                result.extend([key]*count)
            else:
                pass
            
        return result