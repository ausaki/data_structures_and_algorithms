# title: maximum-frequency-stack
# detail: https://leetcode.com/submissions/detail/405796951/
# datetime: Thu Oct  8 02:11:11 2020
# runtime: 304 ms
# memory: 22.4 MB

class FreqStack:

    def __init__(self):
        self.stacks = collections.Counter()
        self.freqs = collections.defaultdict(list)
        self.max_freq = -1
        
    def push(self, x: int) -> None:
        self.stacks[x] += 1
        freq = self.stacks[x]
        if freq > self.max_freq:
            self.max_freq = freq
        self.freqs[freq].append(x)

    def pop(self) -> int:
        x = self.freqs[self.max_freq].pop()
        self.stacks[x] -= 1
        if not self.freqs[self.max_freq]:
            self.max_freq -= 1
        return x
                        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()