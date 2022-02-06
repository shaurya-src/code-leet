class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct = {}
        stack = []
        
        for num in reversed(nums2):
            if len(stack) == 0:
                dct[num] = -1
                stack.append(num)
            else:
                while(len(stack) > 0 and num > stack[-1]):
                    del stack[-1]
                
                if len(stack) > 0 and num < stack[-1]:
                    dct[num] = stack[-1]
                else:
                    dct[num] = -1
                    
                stack.append(num)
        
        return [dct[query] for query in nums1]