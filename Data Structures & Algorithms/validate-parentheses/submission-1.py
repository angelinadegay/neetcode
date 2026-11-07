class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = "([{"
        pairs = {
             ")": "(",
              "]": "[",
             "}": "{"
            }

        for c in s:
            if c in open:
                stack.append(c)

            else:
                if len(stack) > 0 and stack[-1] == pairs[c]:
                    stack.pop()
            
                else:
                    return False
        return  len(stack) == 0