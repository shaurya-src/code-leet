class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.top = -1

    def push(self, x: int) -> None:
        if self.top < self.maxSize-1:
            self.stack.append(x)
            self.top += 1
        else:
            pass

    def pop(self) -> int:
        if self.top == -1:
            return self.top
        else:
            temp = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            return temp

    def increment(self, k: int, val: int) -> None:
        if k > self.top + 1:
            k = self.top + 1
        for i in range(k):
            self.stack[i] += val
            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)