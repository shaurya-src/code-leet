class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = {}
        for num in A:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            
        for key, value in count.items():
            if value == len(A)//2:
                return key