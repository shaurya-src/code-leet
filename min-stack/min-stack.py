class MinStack:
    # Keep track of min associated with each element
    # Push the value and min_till_now
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][-1])))

    def pop(self) -> None:
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()