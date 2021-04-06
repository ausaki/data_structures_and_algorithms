# title: sum-of-beauty-of-all-substrings
# detail: https://leetcode.com/submissions/detail/464255058/
# datetime: Sat Mar  6 22:57:15 2021
# runtime: 2828 ms
# memory: 14.2 MB

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            # mi, ma = 1, 1
            cnt = collections.Counter(s[i])
            for j in range(i + 1, n):
                # c = cnt[s[j]]
                # c += 1
                # if c > ma:
                #     ma = c
                # if c < mi:
                #     mi = c
                # res += ma - mi
                cnt[s[j]] += 1
                res += max(cnt.values()) - min(cnt.values())
                
        return res