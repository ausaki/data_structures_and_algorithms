# title: finding-the-users-active-minutes
# detail: https://leetcode.com/submissions/detail/476157059/
# datetime: Sun Apr  4 10:36:52 2021
# runtime: 996 ms
# memory: 24 MB

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        g = collections.defaultdict(set)
        for i, t in logs:
            g[i].add(t)
        res = [0] * k
        for v in g.values():
            res[len(v) - 1] += 1
        return res