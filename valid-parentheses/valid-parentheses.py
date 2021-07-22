from collections import deque
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_open = ['(', '{', '[']
        p_close = [')', '}', ']']
        stack = deque()
        flag = True
        
        if len(s) <= 1 or s[0] in p_close:
            return False
        
        for x in s:
            if x in p_open:
                stack.append(x)
            elif x in p_close:
                if len(stack) >= 1:
                    if x == ')':
                        if stack[-1] != '(':
                            flag = False
                            break
                        else:
                            stack.pop()
                    if x == ']':
                        if stack[-1] != '[':
                            flag = False
                            break
                        else:
                            stack.pop()
                    if x == '}':
                        if stack[-1] != '{':
                            flag = False
                            break
                        else:
                            stack.pop()
                else:
                    flag = False
                    break
                        
            else:
                flag = False
                break
        return flag and not len(stack)
            