class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # s.reverse()
        left = 0
        right = len(s) - 1
        
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1