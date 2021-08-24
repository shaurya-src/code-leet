class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        if k>len(nums):
            return -1
        return nums[-k]