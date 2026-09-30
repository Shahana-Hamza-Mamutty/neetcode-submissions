class Solution:
    def isValid(self, s: str) -> bool:
        brace_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        if len(s) == 0:
            return True

        stack = []
        for i in list(s):
            if brace_map.get(i) and len(stack) > 0 and stack[-1] == brace_map.get(i):
                stack.pop()
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        
        return False
        