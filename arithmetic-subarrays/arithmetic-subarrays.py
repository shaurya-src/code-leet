class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for l, r in zip(l, r):
            arr = sorted(nums[l:r+1])
            diff = arr[0] - arr[1]
            flag = True
            for i in range(1, len(arr)-1):
                curr = arr[i] - arr[i+1]
                if curr != diff:
                    flag = False
                    break
            res.append(flag)
        
        return res