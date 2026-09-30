class Solution:
  

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
                continue
            
            # print("====", stack)
            right = int(stack.pop())
            left = int(stack.pop())
            # print("====", left, right)

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            else:
                result = int(left / right)  # truncate toward zero
            
            stack.append(result)

        print(stack)
        return int(stack[0])


