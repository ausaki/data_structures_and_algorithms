# title: largest-values-from-labels
# detail: https://leetcode.com/submissions/detail/397544538/
# datetime: Sat Sep 19 01:49:44 2020
# runtime: 152 ms
# memory: 18 MB

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        g = []
        for v, l in zip(values, labels):
            g.append([v, l])
        g.sort()
        cnt = collections.Counter()
        t = 0
        result = 0
        while g and t < num_wanted:
            v, l = g.pop()
            if cnt[l] < use_limit:
                t += 1
                cnt[l] += 1
                result += v
        return result
        