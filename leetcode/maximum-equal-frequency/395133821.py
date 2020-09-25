# title: maximum-equal-frequency
# detail: https://leetcode.com/submissions/detail/395133821/
# datetime: Sun Sep 13 23:58:46 2020
# runtime: 884 ms
# memory: 21.3 MB

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt = collections.Counter()
        vals = collections.Counter()
        result = 1
        for i, j in enumerate(nums):
            if j in cnt:
                vals[cnt[j]] -= 1
                if vals[cnt[j]] == 0:
                    vals.pop(cnt[j])
            cnt[j] += 1
            vals[cnt[j]] += 1
            if len(cnt) == 1 or ((len(vals) == 1 and 1 in vals) or len(vals) == 2 and (vals.get(1, 0) == 1 or (max(vals) - min(vals) == 1 and vals[max(vals)] == 1))):
                result = max(result, i + 1)
        return result
            