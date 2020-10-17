# title: alert-using-same-key-card-three-or-more-times-in-a-one-hour-period
# detail: https://leetcode.com/submissions/detail/409514684/
# datetime: Sat Oct 17 01:09:15 2020
# runtime: 660 ms
# memory: 38.2 MB

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