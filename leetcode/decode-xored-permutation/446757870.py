# title: decode-xored-permutation
# detail: https://leetcode.com/submissions/detail/446757870/
# datetime: Sat Jan 23 23:54:19 2021
# runtime: 1764 ms
# memory: 33.4 MB

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        m = 0
        for i in range(1, n + 1):
            m ^= i
        curr = 0
        for i in range(0, n - 1, 2):
            curr ^= encoded[i]
        last = m ^ curr
        res = [last]
        for i in range(n - 2, -1, -1):
            last ^= encoded[i]
            res.append(last)
        return res[::-1]
        