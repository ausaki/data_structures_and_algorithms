# title: design-a-stack-with-increment-operation
# detail: https://leetcode.com/submissions/detail/385697982/
# datetime: Mon Aug 24 23:26:16 2020
# runtime: 136 ms
# memory: 14.4 MB

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1
    
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)