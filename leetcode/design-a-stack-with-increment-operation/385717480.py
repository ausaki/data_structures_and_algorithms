# title: design-a-stack-with-increment-operation
# detail: https://leetcode.com/submissions/detail/385717480/
# datetime: Tue Aug 25 00:16:36 2020
# runtime: 88 ms
# memory: 14.7 MB

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        
    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return
        self.stack.append([x, 0])

    def pop(self) -> int:
        if not self.stack:
            return -1
        val, inc = self.stack.pop()
        val += inc
        if self.stack:
            self.stack[-1][1] += inc
        return val    
    
    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack)) - 1
        if k < 0 or val == 0:
            return
        self.stack[k][1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)