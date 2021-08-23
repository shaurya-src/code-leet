class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # count distinct numbers
        # if less than 3: return max(x)
        # else: return 3rd max from set
        # sort and return x[2]
        # O(n)?
        # 3 variables: and keep track while iterating?
        
        x = list(set(nums))
        
        if len(x)<3:
            return max(x)
        
        x.sort(reverse=True)
        return x[2]
        