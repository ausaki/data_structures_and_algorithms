# title: find-kth-bit-in-nth-binary-string
# detail: https://leetcode.com/submissions/detail/378722617/
# datetime: Mon Aug 10 13:17:08 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return '0'
        l = (1 << (n - 1)) - 1
        if k <= l:
            return self.findKthBit(n - 1, k)
        if k == l + 1:
            return '1'
        bit = self.findKthBit(n - 1, 2 * l - k + 2)
        return '1' if bit == '0' else '0'