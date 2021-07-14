class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Naive O(n)
        
        # return nums.index(target)
        
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        
        # Optimal O(log n)
        
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
        