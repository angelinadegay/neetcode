class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        curr_min = val if not self.min_stack else min(val, self.min_stack[-1])
        self.min_stack.append(curr_min)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        else:
            return None       

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None
