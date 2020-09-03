# title: xor-operation-in-an-array
# detail: https://leetcode.com/submissions/detail/379887900/
# datetime: Wed Aug 12 22:27:32 2020
# runtime: 28 ms
# memory: 13.8 MB

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result