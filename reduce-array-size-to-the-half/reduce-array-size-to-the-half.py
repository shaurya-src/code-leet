class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = {}
        for num in arr:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        # print(counter.items())
        count = sorted(counter.values(), reverse=True)
        # print(count)
        
        min_size = 0
        exp = len(arr)/2
        reduction = 0
        
        for value in count:
            if reduction >= exp:
                break
            else:
                min_size += 1
                reduction += value
        
        return min_size
                
        