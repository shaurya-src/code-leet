class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg, result = [], [], []
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        z = min(len(pos), len(neg))
        for i in range(z):
            result.extend([pos[i], neg[i]])
        
        result += pos[z:] + neg[z:]
        return result