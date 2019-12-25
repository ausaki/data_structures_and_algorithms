# title: friend-circles
# detail: https://leetcode.com/submissions/detail/286883677/
# datetime: Wed Dec 18 22:41:37 2019
# runtime: 196 ms
# memory: 13.3 MB

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(i):
            for j, k in enumerate(M[i]):
                if j not in seen and k == 1:
                    seen.add(j)
                    dfs(j)
        seen = set()
        res = 0
        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                res += 1
        return res