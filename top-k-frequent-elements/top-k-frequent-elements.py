class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        x = sorted(list(counter.items()), key = lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(x[i][0])
        
        return res