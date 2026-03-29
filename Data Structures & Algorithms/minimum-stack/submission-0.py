class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        

    def pop(self) -> None:
        del self.stack[-1]
        

    def top(self) -> int:
        val = self.stack[-1]
        return val
        

    def getMin(self) -> int:
        return min(self.stack)

        
