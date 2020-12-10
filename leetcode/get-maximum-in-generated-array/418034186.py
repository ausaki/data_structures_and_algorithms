# title: get-maximum-in-generated-array
# detail: https://leetcode.com/submissions/detail/418034186/
# datetime: Sun Nov  8 16:34:50 2020
# runtime: 16 ms
# memory: 14 MB

class Solution:
    arr = [0, 1]
    max_ = [0, 1]
    def getMaximumGenerated(self, n: int) -> int:
        for i in range(len(self.arr), n + 1):
            self.arr.append(self.arr[i // 2] + (self.arr[i // 2 + 1] if i % 2 else 0))
            self.max_.append(max(self.max_[-1], self.arr[-1]))
        return self.max_[n]