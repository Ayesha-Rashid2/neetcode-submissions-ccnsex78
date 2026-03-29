class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}

        for item in tokens:
            if item not in ops:
                stack.append(int(item))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if item == '+':
                    stack.append(val2 + val1)
                elif item == '-':
                    stack.append(val2 - val1)
                elif item == '*':
                    stack.append(val2 * val1)
                elif item == '/':
                    stack.append(int(val2 / val1))

        return stack[0]