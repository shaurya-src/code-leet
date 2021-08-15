class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        repeated = -1
        n = len(nums)
        
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                repeated = num
        
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        
        missing = expected_sum - (actual_sum - repeated)
        
        return [repeated, missing]