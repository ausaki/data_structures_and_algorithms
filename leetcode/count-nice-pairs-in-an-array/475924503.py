# title: count-nice-pairs-in-an-array
# detail: https://leetcode.com/submissions/detail/475924503/
# datetime: Sat Apr  3 22:52:28 2021
# runtime: 864 ms
# memory: 24.5 MB

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        cnt = collections.Counter()
        res = 0
        for i in nums:
            j = int(''.join(reversed(str(i))))
            k = i - j
            res = (res + cnt[k]) % MOD
            cnt[k] += 1
        return res