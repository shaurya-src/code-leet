class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        result = []
        high = len(s)
        low = 0
        for val in s:
            if val == "I":
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
                
        if s[-1] == 'I':
            result.append(low)
        else:
            result.append(high)
        return result