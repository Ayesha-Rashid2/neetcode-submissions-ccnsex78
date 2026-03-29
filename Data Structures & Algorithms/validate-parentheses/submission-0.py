class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")": "(", "]": "[", "}": "{"}
        stack = []

        for st in s:
            if st in valid:
                if stack and stack[-1] == valid[st]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(st)
        if not stack:
            return True
        else:
            return False


        
            
        