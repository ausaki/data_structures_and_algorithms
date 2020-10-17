# title: maximum-frequency-stack
# detail: https://leetcode.com/submissions/detail/405791992/
# datetime: Thu Oct  8 01:56:59 2020
# runtime: 372 ms
# memory: 22.3 MB

class FreqStack:

    def __init__(self):
        self.stacks = collections.Counter()
        self.q = []
        self.i = -1
        
    def push(self, x: int) -> None:
        self.stacks[x] += 1
        heapq.heappush(self.q, (-self.stacks[x], self.i, x))
        self.i -= 1

    def pop(self) -> int:
        freq, _, x = heapq.heappop(self.q)
        self.stacks[x] -= 1
        return x
                        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()