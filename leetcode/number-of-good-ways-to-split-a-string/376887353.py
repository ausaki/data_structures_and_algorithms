# title: number-of-good-ways-to-split-a-string
# detail: https://leetcode.com/submissions/detail/376887353/
# datetime: Thu Aug  6 16:18:48 2020
# runtime: 284 ms
# memory: 14.5 MB

class Solution:
    def numSplits(self, s: str) -> int:
        left = set()
        right_counter = collections.Counter(s)
        right_cnt = len(right_counter)
        result = 0
        for i in range(len(s) - 1):
            left.add(s[i])
            right_counter[s[i]] -= 1
            if right_counter[s[i]] == 0:
                right_cnt -= 1
            if len(left) == right_cnt:
                result += 1
        return result