class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        occur = set()
        result = []
        
        for num in nums:
            if num in occur:
                result.append(num)
            else:
                occur.add(num)
        
        return result