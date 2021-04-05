class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        op = []
        for i in range(len(nums)):
            cr = 0
            for j in range(len(nums)):
                if i!=j and nums[j] < nums[i]:
                    cr +=1
            op.append(cr)
        return op