# title: circular-permutation-in-binary-representation
# detail: https://leetcode.com/submissions/detail/394615162/
# datetime: Sat Sep 12 22:15:02 2020
# runtime: 596 ms
# memory: 107.3 MB

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def dfs(i):
            if len(p) == 1 << n:
                a = p[0] ^ p[1]
                return a and a & (a - 1) == 0
            j = 1
            for _ in range(n):
                k = i ^ j
                if k not in visited:
                    visited.add(k)
                    p.append(k)
                    if dfs(k):
                        return True
                    visited.remove(k)
                    p.pop()
                j <<= 1
            return False
        
        visited = {start}
        p = [start]
        dfs(start)
        return p