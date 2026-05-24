import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda x, y: int(x / y)
        }

        for n in tokens:
            if n in ops:
                y = int(stack.pop())
                x = int(stack.pop())
                res = ops[n](x,y)
                stack.append(res)
            else:
                stack.append(n)
        return int(stack[0])