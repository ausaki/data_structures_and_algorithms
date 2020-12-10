# title: design-an-ordered-stream
# detail: https://leetcode.com/submissions/detail/420750852/
# datetime: Mon Nov 16 12:27:45 2020
# runtime: 208 ms
# memory: 14.7 MB

class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.i = 0

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.arr[id] = value
        if id != self.i:
            return []
        ans = []
        while self.i < len(self.arr) and self.arr[self.i]:
            ans.append(self.arr[self.i])
            self.i += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)