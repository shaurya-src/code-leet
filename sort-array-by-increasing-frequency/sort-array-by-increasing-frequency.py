class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        arr = sorted([[key, value] for key, value in count.items()], reverse = True)
        arr.sort(key = lambda x: x[-1])
        
        res = []
        for num, freq in arr:
            res.extend([num]*freq)
            
        return res