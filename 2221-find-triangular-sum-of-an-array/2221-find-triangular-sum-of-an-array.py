class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        length = len(nums)
        
        for k in range(length - 1):
            i, n = 0, len(nums)
            arr = []
            while i < n-1:
                arr.append((nums[i] + nums[i+1])%10)
                i += 1
            nums[:] = arr
        return nums[0]