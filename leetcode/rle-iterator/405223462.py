# title: rle-iterator
# detail: https://leetcode.com/submissions/detail/405223462/
# datetime: Tue Oct  6 18:31:14 2020
# runtime: 36 ms
# memory: 14.7 MB

class RLEIterator:

    def __init__(self, A: List[int]):
        self.A = A
        self.i = 0

    def next(self, n: int) -> int:
        for j in range(self.i, len(self.A), 2):
            if n > self.A[j]:
                n -= self.A[j]
                self.i = j + 2
            else :
                self.A[j] -= n
                self.i = j if self.A[j] != 0 else j + 2
                return self.A[j + 1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)