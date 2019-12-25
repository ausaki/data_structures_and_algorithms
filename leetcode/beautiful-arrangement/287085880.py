# title: beautiful-arrangement
# detail: https://leetcode.com/submissions/detail/287085880/
# datetime: Thu Dec 19 17:28:00 2019
# runtime: 332 ms
# memory: 12.6 MB

class Solution:
    def countArrangement(self, N: int) -> int:
        def arrange(n):
            if n == 0: return 1
            res = 0
            for i in range(1, N + 1):
                if (n % i == 0 or i % n == 0) and i not in used:
                    used.add(i)
                    res += arrange(n - 1)
                    used.remove(i)
            return res
        used = set()
        return arrange(N)