class Solution:
    def isValid(self, s: str) -> bool:
        pairs = []
        for c in s:
            if c in "([{":
                pairs.append(c)
            else:
                if not pairs:
                    return False
                    
                top = pairs.pop()
        
                if (top == '(' and c != ')') or \
                    (top == '[' and c != ']') or \
                    (top == '{' and c != '}'):
                        return False
        return len(pairs) == 0
