class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr)%2 == 0:
            limit = len(arr) - 1
        else:
            limit = len(arr)
        
        total = sum(arr)
        pos = list(range(3, limit+1, 2))
        
        
        for rng in pos:
            for i in range(len(arr)-rng+1):
                total += sum(arr[i:i+rng])
        return total