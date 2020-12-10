# title: kth-smallest-instructions
# detail: https://leetcode.com/submissions/detail/415460755/
# datetime: Sun Nov  1 12:26:20 2020
# runtime: 40 ms
# memory: 14.1 MB

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        def find(h, v, k):
            n = v - 1
            m = 0
            c = 1
            while k > c:
                k -= c
                n += 1
                m += 1
                c = c * n // m
            if k == c:
                return ((1 << v) - 1) << m
            return (1 << n) | find(m, n - m, k)
        a = find(destination[1], destination[0], k)
        return ''.join('V' if (a >> i) & 1 else 'H' for i in reversed(range(sum(destination))))
