# title: best-team-with-no-conflicts
# detail: https://leetcode.com/submissions/detail/410143461/
# datetime: Sun Oct 18 14:26:33 2020
# runtime: 8296 ms
# memory: 119 MB

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        g = collections.defaultdict(collections.Counter)
        for a, s in zip(ages, scores):
            g[a][s] += 1
        for a, s in g.items():
            prefixsum = []
            prev = 0
            for ss, cnt in sorted(s.items()):
                prev += ss * cnt
                prefixsum.append([ss, prev])
            g[a] = prefixsum
        sorted_ages = sorted(g)
        n = len(sorted_ages)
        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 0
            scores = g[sorted_ages[i]]
            result = dp(i + 1, j)
            k = bisect.bisect_left(scores, [j])
            if k == len(scores):
                return result
            base = scores[k - 1][1] if k else 0
            for l in range(k, len(scores)):
                result = max(result, scores[l][1] - base + dp(i + 1, scores[l][0]))
            return result
        return dp(0, 0)