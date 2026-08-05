class MinStack:

    def __init__(self):
        self.stack = []
        self.stackTop = -1

    def push(self, value: int) -> None:
        newMin = value
        if self.stackTop > -1:
            newMin = min(value, self.stack[self.stackTop][1])
        if self.stackTop + 1 < len(self.stack):
            self.stackTop += 1
            self.stack[self.stackTop] = [value, newMin]
        else:
            self.stack.append([value, newMin])
            self.stackTop += 1

    def pop(self) -> None:
        if self.stackTop > -1:
            self.stackTop -= 1

    def top(self) -> int:
        if self.stackTop > -1:
            num = self.stack[self.stackTop][0]
            return num

    def getMin(self) -> int:
        if self.stackTop > -1:
            num = self.stack[self.stackTop][1]
            return num


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
