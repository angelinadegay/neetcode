class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            else:
                l1= stack.pop()
                l2 = stack.pop()
                
                if c == "+":
                    res = l2 + l1
                elif c == "-":
                    res = l2 - l1
                elif c == "*":
                    res = l2 * l1
                elif c == "/":
                    res = int(l2 / l1)
                
                stack.append(res)
        return stack[0]