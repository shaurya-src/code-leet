class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s = list(s)
        stack = []
        res = ""
        for elem in s:
            if len(stack) == 0 and elem == '(':
                stack.append(elem)
            
            elif len(stack) == 1 and elem == ')':
                del stack[0]
             
            else:
                if elem == '(':
                    stack.append(elem)
                else:
                    del stack[-1]
                
                res += elem
            
        
        return res