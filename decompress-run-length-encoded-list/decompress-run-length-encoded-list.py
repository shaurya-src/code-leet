class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        op = []
        cf = nums[0]
        i = 1
        while i <= (len(nums)):
            try:
                op.extend([nums[i]]*cf)
                cf = nums[i+1]
                i+=2
            except Exception:
                break
        return op