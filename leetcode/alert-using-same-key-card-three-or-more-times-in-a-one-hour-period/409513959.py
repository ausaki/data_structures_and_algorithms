# title: alert-using-same-key-card-three-or-more-times-in-a-one-hour-period
# detail: https://leetcode.com/submissions/detail/409513959/
# datetime: Sat Oct 17 01:06:45 2020
# runtime: 700 ms
# memory: 38.5 MB

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        g = collections.defaultdict(list)
        for name, time in zip(keyName, keyTime):
            h, m = time.split(':')
            g[name].append(int(h) * 60 + int(m))
        result = []
        for name, times in g.items():
            times.sort()
            for i, t in enumerate(times):
                if i >= 2 and t - times[i - 2] <= 60:
                    result.append(name)
                    break
        result.sort()
        return result