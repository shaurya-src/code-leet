class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        curr = 0
        
        for alt in gain:
            curr += alt
            if max_alt < curr:
                max_alt = curr
                
        return max_alt