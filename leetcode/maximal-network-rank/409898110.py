# title: maximal-network-rank
# detail: https://leetcode.com/submissions/detail/409898110/
# datetime: Sun Oct 18 01:48:52 2020
# runtime: 312 ms
# memory: 15.7 MB

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
        idx = sorted(range(n), key=cnt.__getitem__)
        m = len(idx)
        for i in range(m - 2, -1, -1):
            if cnt[idx[i]] != cnt[idx[-1]]:
                break
        if i == m - 2:
            for j in range(i, -1, -1):
                if cnt[idx[j]] != cnt[idx[i]]:
                    break
                a, b = idx[-1], idx[j]
                if a > b:
                    a, b = b, a
                c = a * n + b
                result = max(result, cnt[a] + cnt[b] - (c in pairs))
            return result
        for i, j in itertools.combinations(range(i + 1, m), 2):
            a, b = idx[i], idx[j]
            if a > b:
                a, b = b, a
            c = a * n + b
            result = max(result, cnt[a] + cnt[b] - (c in pairs))
        return result
        