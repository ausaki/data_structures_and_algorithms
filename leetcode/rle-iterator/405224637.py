# title: rle-iterator
# detail: https://leetcode.com/submissions/detail/405224637/
# datetime: Tue Oct  6 18:36:25 2020
# runtime: 32 ms
# memory: 14.4 MB

class RLEIterator:

    def __init__(self, A: List[int]):
        self.A = A
        self.i = 0

    def next(self, n: int) -> int:
        i, A = self.i, self.A
        while i < len(A) and n > A[i]:
            n -= A[i]
            i += 2
        self.i = i
        if i < len(A):
            A[i] -= n
            return A[i + 1]
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)