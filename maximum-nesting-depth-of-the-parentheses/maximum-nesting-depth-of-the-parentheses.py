from collections import deque
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        stack = deque()
        
        if len(s)<2:
            return 0
        
        for char in s:
            if char == '(':
                stack.append('(')
                count = max(count, len(stack))
            elif char == ')':
                stack.pop()
            else:
                pass
        
        return count