class MyQueue:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        newSt = []
        while self.st:
            newSt.append(self.st.pop())
        top = newSt.pop()
        while newSt:
            self.st.append(newSt.pop())
        return top

    def peek(self) -> int:
        newSt = []
        while self.st:
            newSt.append(self.st.pop())
        top = newSt[-1]
        while newSt:
            self.st.append(newSt.pop())
        return top

    def empty(self) -> bool:
        return len(self.st) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
