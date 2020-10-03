# title: number-of-squareful-arrays
# detail: https://leetcode.com/submissions/detail/401462407/
# datetime: Mon Sep 28 01:53:49 2020
# runtime: 32 ms
# memory: 14.2 MB

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        n = len(A)
        g = collections.defaultdict(list)
        for i, a in enumerate(A):
            for j in range(i + 1, n):
                k = math.sqrt(A[i] + A[j])
                if k == int(k):
                    g[i].append(j)
                    g[j].append(i)
        
        def dfs(i):
            visited.add(i)
            if len(visited) == n:
                visited.remove(i)
                return 1
            result = 0
            s = set()
            for j in g[i]:
                if j not in visited and A[j] not in s:
                    s.add(A[j])
                    result += dfs(j)
            visited.remove(i)
            return result
        s = set()
        visited = set()
        result = 0
        for i in range(n):
            if A[i] not in s:
                s.add(A[i])
                result += dfs(i)
        return result
        