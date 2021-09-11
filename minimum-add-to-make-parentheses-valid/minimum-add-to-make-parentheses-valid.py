class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        rest = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if len(stack) >= 1:
                    del stack[-1]
                else:
                    rest += 1
            
        return len(stack) + rest