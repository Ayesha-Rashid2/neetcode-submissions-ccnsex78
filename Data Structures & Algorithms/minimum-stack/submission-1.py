class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

        

    def pop(self) -> None:
        del self.stack[-1]
        

    def top(self) -> int:
        val = self.stack[-1]
        return val
        

    def getMin(self) -> int:
        return min(self.stack)

