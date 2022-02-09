class MyQueue:

    def __init__(self):
        self.stack = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack: return None
        for i in range(len(self.stack) - 1):
            x = self.stack.pop()
            self.s2.append(x)
        res = self.stack.pop()
        # print(res,self.s2)
        for i in range(len(self.s2)):
            x = self.s2.pop()
            self.stack.append(x)
        # print(self.stack)
        return res

    def peek(self) -> int:
        if not self.stack: return None
        n = len(self.stack)
        for i in range(n - 1):
            x = self.stack.pop()
            self.s2.append(x)
        res = self.stack.pop()
        self.s2.append(res)
        for i in range(len(self.s2)):
            x = self.s2.pop()
            self.stack.append(x)
        return res

    def empty(self) -> bool:
        return not self.stack and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()