class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # divide into 2 cases
        # one where elements are just moved fwd.
        # elements which rotate front back to front
        # elements from n-k will start the array
        # array from 0 till n-k-1 will start from k
        # in-place rotation?
        # ar[:] = x will overwrite the existing object
        # ar = x tries to point ar to new object addr. of x
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]