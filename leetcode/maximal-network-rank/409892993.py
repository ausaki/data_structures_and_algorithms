# title: maximal-network-rank
# detail: https://leetcode.com/submissions/detail/409892993/
# datetime: Sun Oct 18 01:32:34 2020
# runtime: 332 ms
# memory: 15.4 MB

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        pairs = set()
        cnt = [0] * n
        for a, b in roads:
            if a > b:
                a, b = b, a
            pairs.add(a * n + b)
            cnt[a] += 1
            cnt[b] += 1
        result = 0
        for a, b in itertools.combinations(range(n), 2):
            if a > b:
                a, b = b, a
            c = a * n + b
            result = max(result, cnt[a] + cnt[b] - (c in pairs))
        return result
        