class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        num_stack = []
        for token in tokens:
            if len(token)>1 or token.isdigit():
                num_stack.append(int(token))
            else:
                if token =="+":
                    num_stack[-2] += num_stack[-1]
                elif token =="-":
                    num_stack[-2]-= num_stack[-1]
                elif token == "*":
                    num_stack[-2]*= num_stack[-1]
                else:
                    num_stack[-2] = int(float(num_stack[-2]) / num_stack[-1])
                num_stack.pop()
        return num_stack[0]