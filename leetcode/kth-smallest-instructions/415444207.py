# title: kth-smallest-instructions
# detail: https://leetcode.com/submissions/detail/415444207/
# datetime: Sun Nov  1 11:41:12 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        def find(h, v, k):
            if k == 1:
                return 'H' * h + 'V' * v
            k -= 1
            n = v
            m = 1
            c = v
            while k > c:
                k -= c
                n += 1
                m += 1
                c = c * n // m
            if k == c:
                return 'H' * (h - m) + 'V' * v + 'H' * m
            return 'H' * (h - m) + 'V' + find(m, n - m, k)
        return find(destination[1], destination[0], k)