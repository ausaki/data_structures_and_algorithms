# title: maximum-frequency-stack
# detail: https://leetcode.com/submissions/detail/405786337/
# datetime: Thu Oct  8 01:41:24 2020
# runtime: 384 ms
# memory: 22.1 MB

class FreqStack:

    def __init__(self):
        self.stacks = collections.defaultdict(list)
        self.q = []
        self.i = -1
        
    def push(self, x: int) -> None:
        self.stacks[x].append(self.i)
        heapq.heappush(self.q, (-len(self.stacks[x]), self.i, x))
        self.i -= 1

    def pop(self) -> int:
        freq, _, x = heapq.heappop(self.q)
        s = self.stacks[x]
        s.pop()
        if s:
            heapq.heappush(self.q, (len(s), s[-1], x))
        else:
            self.stacks.pop(x)
        return x
                        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()