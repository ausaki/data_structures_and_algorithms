# title: fancy-sequence
# detail: https://leetcode.com/submissions/detail/410581574/
# datetime: Mon Oct 19 16:24:29 2020
# runtime: 2616 ms
# memory: 93.2 MB

class Fancy:
    MOD = 10 ** 9 + 7
    
    def __init__(self):
        self.seq = []
        self.actions = [[0, [1, 0]]]

    def append(self, val: int) -> None:
        self.seq.append(val)

    def addAll(self, inc: int) -> None:
        l = len(self.seq)
        if l == 0:
            return
        if self.actions[-1][0] != l:
            self.actions.append([l, self.actions[-1][1][:]])
        self.actions[-1][1][1] += inc

    def multAll(self, m: int) -> None:
        l = len(self.seq)
        if l == 0:
            return
        if self.actions[-1][0] != l:
            self.actions.append([l, self.actions[-1][1][:]])
        actions = self.actions[-1][1]
        actions[0] = actions[0] * m
        actions[1] = actions[1] * m
            
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        i = bisect.bisect(self.actions, [idx + 1])        
        val = self.seq[idx]
        m1, inc1 = self.actions[i - 1][1]
        m2, inc2 = self.actions[-1][1]
        m = m2 // m1
        inc = inc2 - inc1 * m
        val = (val * m + inc) % self.MOD
        return val
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)