class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfs(candidates, target, [], result)
        return result
    
    def dfs(self, nums, target, path, result):
        if target < 0:
            return None
        
        if target == 0:
            result.append(path)
            return None
        
        for i, num in enumerate(nums):
            remain = target - num
            self.dfs(nums[i:], remain, path+[num], result)