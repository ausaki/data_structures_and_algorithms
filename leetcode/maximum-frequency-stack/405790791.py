# title: maximum-frequency-stack
# detail: https://leetcode.com/submissions/detail/405790791/
# datetime: Thu Oct  8 01:53:44 2020
# runtime: 352 ms
# memory: 21.8 MB

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
        if not s:
            self.stacks.pop(x)
        return x
                        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()