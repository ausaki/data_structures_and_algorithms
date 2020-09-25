# title: dinner-plate-stacks
# detail: https://leetcode.com/submissions/detail/396505623/
# datetime: Wed Sep 16 16:42:11 2020
# runtime: 908 ms
# memory: 74.9 MB

class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = []
        self.idx = []

    def push(self, val: int) -> None:
        if self.idx and 0 <= -self.idx[-1] < len(self.stacks):
            i = -self.idx[-1]
            st = self.stacks[i]
            st.append(val)
            if len(st) == self.cap:
                self.idx.pop()
        else:
            self.idx.clear()
            self.stacks.append([val])
            if self.cap > 1:
                self.idx.append(-len(self.stacks) + 1)                        
        
    def pop(self) -> int:
        if not self.stacks:
            return -1
        st = self.stacks[-1]
        val = st.pop()
        if len(st) == self.cap - 1:
            bisect.insort(self.idx, -len(self.stacks) + 1)
        self._clean()
        return val

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            st = self.stacks[index]
            val = st.pop()
            if len(st) == self.cap - 1:
                bisect.insort(self.idx, -index)
            self._clean()
            return val
        return -1
    
    def _clean(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        
        
# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)